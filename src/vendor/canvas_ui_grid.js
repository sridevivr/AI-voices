/*! Grid effect from Canvas UI (https://github.com/DavidHDev/canvas-ui, commit d5a6778), bundled unmodified.
 * Copyright (c) 2026 David Haz. MIT + Commons Clause License Condition v1.0: use, copy, modify, merge, publish and
 * distribute as part of an application, website or product; the components themselves may not be sold,
 * sublicensed or redistributed, alone, in a bundle, or as a ported version. Full text: src/vendor/CANVAS_UI_LICENSE.md
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND. */
(()=>{var me=new WeakMap;function ce(l,s){let t=window.visualViewport?.scale||1,a=Math.min(window.devicePixelRatio||1,2)*t,f=Math.max(l.clientWidth,1),n=Math.max(l.clientHeight,1),e=8192;if(s){let d=me.get(s);d===void 0&&(d=Math.min(e,s.getParameter(s.MAX_TEXTURE_SIZE),s.getParameter(s.MAX_RENDERBUFFER_SIZE)),me.set(s,d)),e=d}return Math.min(a,e/Math.max(f,n),Math.sqrt(16777216/(f*n)))}function de(l){let s=window.visualViewport,t=0,a=!1,f=()=>{t||a||(t=requestAnimationFrame(()=>{t=0,l()}))},n=new ResizeObserver(f);return window.addEventListener("resize",f,{passive:!0}),s?.addEventListener("resize",f,{passive:!0}),{observe(e,d){n.observe(e,d)},unobserve(e){n.unobserve(e)},disconnect(){a=!0,n.disconnect(),cancelAnimationFrame(t),window.removeEventListener("resize",f),s?.removeEventListener("resize",f)}}}function ve(){return typeof navigator>"u"?!1:navigator.userAgentData?.platform==="Android"||/Android/i.test(navigator.userAgent)}function Te(l,s){"content"in l?(l.setAttribute("content","drawable"),s.setAttribute("drawable","")):l.setAttribute("layoutsubtree","")}var he=new WeakMap;function Ce(l){let s=performance.now(),t=he.get(l);if(t&&s-t.at<500)return t.layers;let a=[];for(let f=l;f;f=f.parentElement){let n=getComputedStyle(f).backgroundColor,e=1;if(!n||n==="transparent")e=0;else{let d=/\/\s*([\d.]+)(%?)\s*\)$/.exec(n),E=/^rgba\(([^)]+)\)$/.exec(n);d?e=Number(d[1])/(d[2]?100:1):E&&(e=Number(E[1].split(",")[3]??1))}if(e>0&&(a.unshift(n),e>=1))break}return he.set(l,{at:s,layers:a}),a}function pe(l,s,t,a=!1){if(a)for(let e of Ce(l))s.fillStyle=e,s.fillRect(0,0,l.width,l.height);let f=s.drawElementImage(t,0,0),n=l;f&&typeof n.updateElementGeometry=="function"&&n.updateElementGeometry(t,{canvasTransform:f})}function Ee(l){let s=l.getBoundingClientRect(),t=()=>{s=l.getBoundingClientRect()},a=new ResizeObserver(t);return a.observe(l),window.addEventListener("resize",t,{passive:!0}),window.addEventListener("scroll",t,{capture:!0,passive:!0}),{get current(){return s},destroy(){a.disconnect(),window.removeEventListener("resize",t),window.removeEventListener("scroll",t,!0)}}}function Z(l,s){let t={};for(let a of Object.keys(s)){let f=s[a];t[a]=f===void 0?l[a]:f}return t}var J={tileSize:150,gap:0,cornerRadius:0,amplitude:2.5,waveSpeed:.5,frequency:12,waveWidth:.05,fadeTime:.6,maxLift:1,jitter:0,liftHeight:60,perspective:1200,tilt:1,shading:.05,tint:[0,.33,1],tintStrength:.1,idleRipples:0},S=64,Le=.03,xe=3,Se=`#version 300 es
precision highp float;
layout(location = 0) in vec2 aPos;
out vec2 vUv;
void main () {
  vUv = aPos * 0.5 + 0.5;
  gl_Position = vec4(aPos, 0.0, 1.0);
}`,_e=`#version 300 es
precision highp float;
out vec4 outColor;
uniform sampler2D uTrail;
uniform int uTrailCount;
uniform float uWorldPerTile;
uniform float uWaveSpeed;
uniform float uFrequency;
uniform float uWaveWidth;
uniform float uFadeTime;
uniform float uAmplitude;
uniform float uJitter;
uniform float uMaxLift;

vec2 hash2 (vec2 p) {
  p = vec2(dot(p, vec2(127.1, 311.7)), dot(p, vec2(269.5, 183.3)));
  return fract(sin(p) * 43758.5453123) - 0.5;
}

void main () {
  vec2 tile = floor(gl_FragCoord.xy);
  vec2 world = (tile + 0.5) * uWorldPerTile + hash2(tile) * uJitter * 0.12;

  float waveHeight = 0.0;
  float totalWeight = 0.0;

  for (int i = 0; i < 64; i++) {
    if (i >= uTrailCount) break;

    vec4 td = texelFetch(uTrail, ivec2(i, 0), 0);
    vec2 delta = world - td.xy;
    float dist = length(delta);
    float relDist = dist - uWaveSpeed * td.z;

    float window = exp(-(relDist * relDist) / (uWaveWidth * uWaveWidth));

    float fade = exp(-td.z / uFadeTime);
    float atten = 1.0 / (1.0 + dist * 3.0);
    float weight = fade * window * atten * td.w;
    waveHeight += weight * cos(uFrequency * relDist);
    totalWeight += weight;
  }

  float lift = clamp(
    waveHeight / max(totalWeight, 1.0) * uAmplitude, -uMaxLift, uMaxLift
  );

  outColor = vec4(lift * 0.5 + 0.5, 0.0, 0.0, 1.0);
}`,ye=`#version 300 es
precision highp float;
in vec2 vUv;
out vec4 outColor;
uniform sampler2D uContent;
uniform sampler2D uTiles;
uniform vec2 uResolution;
uniform ivec2 uGridTiles;
uniform float uTilePx;
uniform float uGapPx;
uniform float uCornerPx;
uniform float uLiftPx;
uniform float uPersp;
uniform vec2 uVanish;
uniform float uShading;
uniform vec3 uTint;
uniform float uTintStrength;
uniform float uMaxX;
uniform float uHasContent;

float tileLift (ivec2 idx) {
  idx = clamp(idx, ivec2(0), uGridTiles - 1);
  return texelFetch(uTiles, idx, 0).r * 2.0 - 1.0;
}

float roundedBox (vec2 p, vec2 b, float r) {
  vec2 q = abs(p) - b + r;
  return length(max(q, 0.0)) + min(max(q.x, q.y), 0.0) - r;
}

float tileSd (vec2 w, ivec2 idx, float halfSize) {
  vec2 center = (vec2(idx) + 0.5) * uTilePx;
  return roundedBox(w - center, vec2(halfSize), min(uCornerPx, halfSize));
}

vec2 unproject (vec2 p, float z) {
  return uVanish + (p - uVanish) * (uPersp - z) / uPersp;
}

void main () {
  if (vUv.x > uMaxX) {
    outColor = vec4(0.0);
    return;
  }

  vec2 pos = vUv * uResolution;
  float halfSize = uTilePx * 0.5 - uGapPx * 0.5;

  float bestZ = -1e6;
  float edgeSd = 1.0;
  ivec2 bestIdx = ivec2(-1);
  vec2 bestW = pos;
  float bestLift = 0.0;
  bool bestIsWall = false;
  vec2 wallN = vec2(0.0);
  ivec2 lastIdx = ivec2(-9999);

  for (int k = 0; k < 8; k++) {
    float probeZ = (float(k) / 3.5 - 1.0) * uLiftPx;
    ivec2 idx = clamp(
      ivec2(floor(unproject(pos, probeZ) / uTilePx)),
      ivec2(0), uGridTiles - 1
    );
    if (all(equal(idx, lastIdx))) continue;
    lastIdx = idx;

    float lift = tileLift(idx);
    float h = lift * uLiftPx;

    if (h <= bestZ) continue;

    vec2 wh = unproject(pos, h);
    float sdTop = tileSd(wh, idx, halfSize);

    if (sdTop < 0.75) {
      bestZ = h;
      edgeSd = sdTop;
      bestIdx = idx;
      bestW = wh;
      bestLift = lift;
      bestIsWall = false;
    } else if (h > 0.0) {
      float sd0 = tileSd(pos, idx, halfSize);
      if (sd0 < 0.75) {
        float za = 0.0;
        float zb = h;
        for (int r = 0; r < 3; r++) {
          float zm = (za + zb) * 0.5;
          float sm = tileSd(unproject(pos, zm), idx, halfSize);
          if (sm < 0.0) { za = zm; } else { zb = zm; }
        }
        float zStar = (za + zb) * 0.5;
        if (zStar > bestZ) {
          vec2 wz = unproject(pos, zStar);
          vec2 e = vec2(0.75, 0.0);
          wallN = normalize(vec2(
            tileSd(wz + e.xy, idx, halfSize) - tileSd(wz - e.xy, idx, halfSize),
            tileSd(wz + e.yx, idx, halfSize) - tileSd(wz - e.yx, idx, halfSize)
          ) + 1e-5);
          bestZ = zStar;
          edgeSd = sd0;
          bestIdx = idx;
          bestW = wz;
          bestLift = lift;
          bestIsWall = true;
        }
      }
    }
  }

  if (bestIdx.x < 0) {
    outColor = vec4(0.0);
    return;
  }
  float mask = 1.0 - smoothstep(-0.75, 0.75, edgeSd);
  if (mask <= 0.0) {
    outColor = vec4(0.0);
    return;
  }

  vec2 tileOrigin = vec2(bestIdx) * uTilePx;
  vec2 samplePos = clamp(bestW, tileOrigin + 0.5, tileOrigin + uTilePx - 0.5);
  vec2 sampleUv = samplePos / uResolution;
  sampleUv.x = min(sampleUv.x, uMaxX - 0.002);
  vec4 content;
  if (uHasContent > 0.5) {
    content = texture(uContent, vec2(sampleUv.x, 1.0 - sampleUv.y));
  } else {
    float liftAmt = clamp(abs(bestLift), 0.0, 1.0);
    content = vec4(
      mix(vec3(0.62), uTint, clamp(uTintStrength, 0.0, 1.0)),
      liftAmt * 0.55);
  }

  float t = clamp(bestLift, 0.0, 1.0) * uTintStrength;
  vec3 col;
  float alpha;

  if (bestIsWall) {
    vec2 lightDir = normalize(vec2(-0.55, 0.8));
    float facing = dot(wallN, lightDir);
    float shade = 1.0 - (0.5 - 0.32 * facing) * uShading;
    col = content.rgb * shade;

    alpha = uHasContent > 0.5 ? max(content.a, 0.85) : min(content.a * 1.5, 0.85);
  } else {
    float gx = tileLift(bestIdx + ivec2(1, 0)) - tileLift(bestIdx - ivec2(1, 0));
    float gy = tileLift(bestIdx + ivec2(0, 1)) - tileLift(bestIdx - ivec2(0, 1));
    float shade = (gy - gx) * 0.25 * uShading;
    shade += clamp(bestLift, -1.0, 1.0) * 0.1 * uShading;
    col = content.rgb * (1.0 + shade * 0.85) + shade * 0.12;
    alpha = clamp(content.a + t + abs(shade) * 0.5, 0.0, 1.0);
  }

  col = mix(col, uTint, t);
  float aOut = alpha * mask;
  outColor = vec4(col * aOut, aOut);
}`;function ge(l,s={}){let t={...J,...Z(J,s)},{source:a,content:f,output:n}=l,e=n.getContext("webgl2",{alpha:!0,depth:!1,stencil:!1,antialias:!1,premultipliedAlpha:!0});if(!e||e.isContextLost())return null;let d=a.getContext("2d"),E=a,b=!!(!ve()&&a.contains(f)&&d&&typeof d.drawElementImage=="function"&&typeof E.requestPaint=="function");b&&Te(a,f);let _=!1,$=()=>{};b&&(E.onpaint=()=>{try{d.reset(),pe(a,d,f),_=!0,$()}catch{}});function Q(i,u){let o=e.createShader(i);return e.shaderSource(o,u),e.compileShader(o),e.getShaderParameter(o,e.COMPILE_STATUS)||console.error("Grid shader error:",e.getShaderInfoLog(o)),o}function K(i){let u=Q(e.VERTEX_SHADER,Se),o=Q(e.FRAGMENT_SHADER,i),r=e.createProgram();e.attachShader(r,u),e.attachShader(r,o),e.linkProgram(r);let c={},L=e.getProgramParameter(r,e.ACTIVE_UNIFORMS);for(let g=0;g<L;g++){let w=e.getActiveUniform(r,g);c[w.name]=e.getUniformLocation(r,w.name)}return{program:r,uniforms:c,vertexShader:u,fragmentShader:o}}let m=K(ye),v=K(_e),ee=e.createBuffer();e.bindBuffer(e.ARRAY_BUFFER,ee),e.bufferData(e.ARRAY_BUFFER,new Float32Array([-1,-1,1,-1,-1,1,1,1]),e.STATIC_DRAW),e.enableVertexAttribArray(0),e.vertexAttribPointer(0,2,e.FLOAT,!1,0,0);let y=e.createTexture();e.bindTexture(e.TEXTURE_2D,y),e.texParameteri(e.TEXTURE_2D,e.TEXTURE_MIN_FILTER,e.LINEAR),e.texParameteri(e.TEXTURE_2D,e.TEXTURE_MAG_FILTER,e.LINEAR),e.texParameteri(e.TEXTURE_2D,e.TEXTURE_WRAP_S,e.CLAMP_TO_EDGE),e.texParameteri(e.TEXTURE_2D,e.TEXTURE_WRAP_T,e.CLAMP_TO_EDGE),e.texImage2D(e.TEXTURE_2D,0,e.RGBA,1,1,0,e.RGBA,e.UNSIGNED_BYTE,new Uint8Array([0,0,0,0]));let R=new Float32Array(S*4),I=e.createTexture();e.bindTexture(e.TEXTURE_2D,I),e.texParameteri(e.TEXTURE_2D,e.TEXTURE_MIN_FILTER,e.NEAREST),e.texParameteri(e.TEXTURE_2D,e.TEXTURE_MAG_FILTER,e.NEAREST),e.texParameteri(e.TEXTURE_2D,e.TEXTURE_WRAP_S,e.CLAMP_TO_EDGE),e.texParameteri(e.TEXTURE_2D,e.TEXTURE_WRAP_T,e.CLAMP_TO_EDGE),e.texImage2D(e.TEXTURE_2D,0,e.RGBA32F,S,1,0,e.RGBA,e.FLOAT,R);function te(){return ce(n,e)}let p=null,x=null,P=0,A=0;function be(){let i=Math.max(t.tileSize,8)*te(),u=Math.max(1,Math.ceil(n.width/i)),o=Math.max(1,Math.ceil(n.height/i));p&&u===P&&o===A||(P=u,A=o,p&&e.deleteTexture(p),x&&e.deleteFramebuffer(x),p=e.createTexture(),e.bindTexture(e.TEXTURE_2D,p),e.texParameteri(e.TEXTURE_2D,e.TEXTURE_MIN_FILTER,e.NEAREST),e.texParameteri(e.TEXTURE_2D,e.TEXTURE_MAG_FILTER,e.NEAREST),e.texParameteri(e.TEXTURE_2D,e.TEXTURE_WRAP_S,e.CLAMP_TO_EDGE),e.texParameteri(e.TEXTURE_2D,e.TEXTURE_WRAP_T,e.CLAMP_TO_EDGE),e.texImage2D(e.TEXTURE_2D,0,e.RGBA,P,A,0,e.RGBA,e.UNSIGNED_BYTE,null),x=e.createFramebuffer(),e.bindFramebuffer(e.FRAMEBUFFER,x),e.framebufferTexture2D(e.FRAMEBUFFER,e.COLOR_ATTACHMENT0,e.TEXTURE_2D,p,0),e.bindFramebuffer(e.FRAMEBUFFER,null))}let ne=1;function N(){let i=te(),u=Math.max(1,Math.round(n.clientWidth*i)),o=Math.max(1,Math.round(n.clientHeight*i));if((n.width!==u||n.height!==o)&&(n.width=u,n.height=o),ne=Math.min(1,Math.max(.05,f.clientWidth/Math.max(n.clientWidth,1))),b){let r=Math.max(1,Math.round(a.clientWidth)),c=Math.max(1,Math.round(a.clientHeight));(a.width!==r*i||a.height!==c*i)&&(a.width=r*i,a.height=c*i),E.requestPaint()}}N();function Re(){!b||!_||(_=!1,e.bindTexture(e.TEXTURE_2D,y),e.texImage2D(e.TEXTURE_2D,0,e.RGBA,e.RGBA,e.UNSIGNED_BYTE,a))}let h=[],U=null,k=xe,D=0;function ie(i){h.length>=S&&h.shift(),h.push(i)}function Me(i){let u=Math.max(t.fadeTime,.1)*4;for(let r=h.length-1;r>=0;r--)h[r].age+=i,h[r].age>u&&h.splice(r,1);if(k+=i,t.idleRipples>0&&k>=xe&&(D+=i,D>=t.idleRipples)){D=0;let r=Math.max(n.clientWidth,1)/Math.max(n.clientHeight,1);ie({x:(.2+Math.random()*.6)*r,y:.2+Math.random()*.6,age:0,strength:.8+Math.random()*.3})}let o=Math.min(h.length,S);for(let r=0;r<o;r++){let c=r*4;R[c]=h[r].x,R[c+1]=h[r].y,R[c+2]=h[r].age,R[c+3]=h[r].strength}return e.bindTexture(e.TEXTURE_2D,I),e.texSubImage2D(e.TEXTURE_2D,0,0,0,S,1,e.RGBA,e.FLOAT,R),o}let F=.5,G=.5,z=.5,X=.5;function we(i,u){Re(),be();let o=n.width/Math.max(n.clientWidth,1),r=Math.max(t.tileSize,8)*o,c=1-Math.exp(-u*4);F+=(z-F)*c,G+=(X-G)*c,e.useProgram(v.program),e.activeTexture(e.TEXTURE0),e.bindTexture(e.TEXTURE_2D,I),e.uniform1i(v.uniforms.uTrail,0),e.uniform1i(v.uniforms.uTrailCount,i),e.uniform1f(v.uniforms.uWorldPerTile,r/n.height),e.uniform1f(v.uniforms.uWaveSpeed,Math.max(t.waveSpeed,.01)),e.uniform1f(v.uniforms.uFrequency,t.frequency),e.uniform1f(v.uniforms.uWaveWidth,Math.max(t.waveWidth,.01)),e.uniform1f(v.uniforms.uFadeTime,Math.max(t.fadeTime,.1)),e.uniform1f(v.uniforms.uAmplitude,t.amplitude),e.uniform1f(v.uniforms.uJitter,t.jitter),e.uniform1f(v.uniforms.uMaxLift,Math.max(t.maxLift,.01)),e.bindFramebuffer(e.FRAMEBUFFER,x),e.viewport(0,0,P,A),e.drawArrays(e.TRIANGLE_STRIP,0,4),e.useProgram(m.program),e.activeTexture(e.TEXTURE0),e.bindTexture(e.TEXTURE_2D,y),e.uniform1i(m.uniforms.uContent,0),e.uniform1f(m.uniforms.uHasContent,b?1:0),e.activeTexture(e.TEXTURE1),e.bindTexture(e.TEXTURE_2D,p),e.uniform1i(m.uniforms.uTiles,1),e.activeTexture(e.TEXTURE0),e.uniform2f(m.uniforms.uResolution,n.width,n.height),e.uniform2i(m.uniforms.uGridTiles,P,A),e.uniform1f(m.uniforms.uTilePx,r),e.uniform1f(m.uniforms.uGapPx,Math.max(t.gap,0)*o),e.uniform1f(m.uniforms.uCornerPx,Math.max(t.cornerRadius,0)*o),e.uniform1f(m.uniforms.uLiftPx,Math.max(t.liftHeight,0)*o),e.uniform1f(m.uniforms.uPersp,Math.max(t.perspective,100)*o),e.uniform2f(m.uniforms.uVanish,(.5+(F-.5)*t.tilt)*n.width,(.5+(.5-G)*t.tilt)*n.height),e.uniform1f(m.uniforms.uShading,t.shading),e.uniform3f(m.uniforms.uTint,t.tint[0],t.tint[1],t.tint[2]),e.uniform1f(m.uniforms.uTintStrength,t.tintStrength),e.uniform1f(m.uniforms.uMaxX,ne),e.bindFramebuffer(e.FRAMEBUFFER,null),e.viewport(0,0,n.width,n.height),e.drawArrays(e.TRIANGLE_STRIP,0,4)}let W=0,q=performance.now(),j=!1,M=!1,H=!0,O=window.matchMedia("(prefers-reduced-motion: reduce)"),C=O.matches;function re(i){if(j)return;if(!H){M=!1;return}let u=Math.min((i-q)/1e3,1/30);q=i;let o=C?0:Me(u);we(o,u);let r=Math.abs(F-z)+Math.abs(G-X)>.001;if(!(!C&&(o>0||t.idleRipples>0||r))&&!_){M=!1;return}W=requestAnimationFrame(re)}function T(){j||M||!H||(M=!0,q=performance.now(),W=requestAnimationFrame(re))}$=T,T();function ae(){C=O.matches,C&&(h.length=0),T()}O.addEventListener("change",ae);let V=de(()=>{N(),T()});V.observe(n),V.observe(f);let oe=!0;function Y(){H=oe&&document.visibilityState!=="hidden",H?T():M&&(cancelAnimationFrame(W),M=!1)}let se=new IntersectionObserver(i=>{oe=i[i.length-1]?.isIntersecting??!0,Y()});document.addEventListener("visibilitychange",Y),se.observe(n);let B=n.parentElement??n,le=Ee(n);function ue(i){if(C)return;let u=le.current,o=Math.max(u.width,1)/Math.max(u.height,1),r=(i.clientX-u.left)/Math.max(u.width,1),c=(i.clientY-u.top)/Math.max(u.height,1);z=r,X=c;let L=r*o,g=1-c,w=.2;if(U){let Pe=L-U.x,Ae=g-U.y;if(w=Math.hypot(Pe,Ae),w<Le){T();return}}ie({x:L,y:g,age:0,strength:Math.min(Math.max(w*6,.25),1.2)}),U={x:L,y:g},k=0,D=0,T()}function fe(){z=.5,X=.5,T()}return B.addEventListener("pointermove",ue,{passive:!0}),B.addEventListener("pointerleave",fe,{passive:!0}),{setOptions(i){i=Z(J,i),Object.entries(i).some(([u,o])=>t[u]!==o)&&(Object.assign(t,i),T())},resize(){N(),T()},destroy(){j=!0,le.destroy(),cancelAnimationFrame(W),V.disconnect(),se.disconnect(),document.removeEventListener("visibilitychange",Y),O.removeEventListener("change",ae),B.removeEventListener("pointermove",ue),B.removeEventListener("pointerleave",fe),e.deleteTexture(y),e.deleteTexture(I),p&&e.deleteTexture(p),x&&e.deleteFramebuffer(x);for(let i of[m,v])e.deleteProgram(i.program),e.deleteShader(i.vertexShader),e.deleteShader(i.fragmentShader);e.deleteBuffer(ee),b&&(E.onpaint=null)}}}window.CanvasUIGrid={createGrid:ge};})();
