(self.webpackChunkai_frontend=self.webpackChunkai_frontend||[]).push([[216,246,214],{54418:function(j,i,e){"use strict";e.r(i);var m=e(70412),d=e(47682),p={text:m.default,imageUrl:d.default,videoUrl:d.default};i.default=p},47682:function(j,i,e){"use strict";e.r(i),e.d(i,{default:function(){return te}});var m=e(30279),d=e.n(m),p=e(94434),U=e.n(p),A=e(35290),f=e.n(A),y=e(411),E=e.n(y),$=e(46686),S=e.n($),v=e(93236),z=e(65713),J=e(41385),I=e(86004),M=e(929),H=e(17986),Q=e(66122),Y=e(61654),w=e(87976);function k(){return P.apply(this,arguments)}function P(){return P=E()(f()().mark(function D(){return f()().wrap(function(g){for(;;)switch(g.prev=g.next){case 0:return g.abrupt("return",w.Z.get("oss/sign"));case 1:case"end":return g.stop()}},D)})),P.apply(this,arguments)}var q=e(47277),_=e(12383),ee=e(17771),ae={preview:"preview___Rqv6O"},R=e(32699),l=e(62086),ne=(0,v.memo)(function(D){var O=D.value,g=D.onChange,L=g===void 0?function(){}:g,ue=(0,v.useState)(),x=S()(ue,2),u=x[0],re=x[1],se=(0,v.useState)(O),F=S()(se,2),o=F[0],B=F[1],le=(0,v.useState)(null),W=S()(le,2),K=W[0],T=W[1],oe=(0,v.useState)("url"),N=S()(oe,2),C=N[0],ie=N[1],de=(0,v.useState)([]),b=S()(de,2),c=b[0],G=b[1],ve=(0,ee.A)({sources:[{src:o}]}),fe=ve.Video,ce=(0,q.Z)(L,{wait:300}),V=ce.run;(0,_.Z)(function(){B(O)},[O]);var X=function(){var n=E()(f()().mark(function a(){var t,r;return f()().wrap(function(s){for(;;)switch(s.prev=s.next){case 0:return s.prev=0,s.next=3,k();case 3:r=s.sent,re(r==null||(t=r.data)===null||t===void 0?void 0:t.data),s.next=11;break;case 7:s.prev=7,s.t0=s.catch(0),console.error(s.t0),z.ZP.error("\u4E0A\u4F20\u5931\u8D25,\u8BF7\u7A0D\u540E\u91CD\u8BD5");case 11:case"end":return s.stop()}},a,null,[[0,7]])}));return function(){return n.apply(this,arguments)}}();(0,v.useEffect)(function(){C==="upload"&&X()},[C]),(0,v.useEffect)(function(){if(c&&c.length){var n=c==null?void 0:c[0];if((n==null?void 0:n.percent)===100){var a,t;B((u==null?void 0:u.host)+"/"+(n==null?void 0:n.url));var r=null;n!=null&&(a=n.type)!==null&&a!==void 0&&a.startsWith("image")&&(r="image"),n!=null&&(t=n.type)!==null&&t!==void 0&&t.startsWith("video")&&(r="video"),T(r)}}},[u,c,L]);var he=function(a){var t=a.fileList,r=t===void 0?[]:t;G(U()(r))},me=function(a){var t=(c||[]).filter(function(r){return r.url!==a.url});G(t)},pe=function(a){return{key:a.url,OSSAccessKeyId:u==null?void 0:u.OSSAccessKeyId,policy:u==null?void 0:u.policy,Signature:u==null?void 0:u.Signature}},ge=function(){var n=E()(f()().mark(function a(t){var r,Z,s;return f()().wrap(function(h){for(;;)switch(h.prev=h.next){case 0:if(u){h.next=2;break}return h.abrupt("return",!1);case 2:if(r=Number(u.expire)*1e3,!(r<Date.now())){h.next=6;break}return h.next=6,X();case 6:return Z=t.name.slice(t.name.lastIndexOf(".")),s=Date.now()+Z,t.url=u.dir+"/"+s,h.abrupt("return",t);case 10:case"end":return h.stop()}},a)}));return function(t){return n.apply(this,arguments)}}(),Ee={name:"file",fileList:c,multiple:!1,maxCount:1,accept:"video/*, image/*",action:u==null?void 0:u.host,onChange:he,onRemove:me,data:pe,beforeUpload:ge},Se=function(a){var t=a.target.value;B(t)};(0,v.useEffect)(function(){o&&((0,R.endsWith)(".mp4",o)&&T("image"),(0,R.endsWith)(".jpg",o)&&T("image"),V(o))},[V,o]);var Ce=function(){var a=null;return o&&K==="image"&&(a=(0,l.jsx)("div",{className:ae.preview,children:(0,l.jsx)(J.Z,{src:o})})),o&&K==="video"&&(a=(0,l.jsx)(fe,{width:400,src:o})),a};return(0,l.jsxs)("div",{children:[Ce(),(0,l.jsxs)(I.Z.Group,{compact:!0,children:[(0,l.jsxs)(M.Z,{value:C,onChange:function(a){return ie(a)},children:[(0,l.jsx)(M.Z.Option,{value:"url",children:"\u8F93\u5165URL"}),(0,l.jsx)(M.Z.Option,{value:"upload",children:"\u672C\u5730\u4E0A\u4F20"})]}),(0,l.jsx)(I.Z,{value:o,onChange:Se,disabled:C==="upload",style:{width:"70%"},placeholder:"\u8BF7\u8F93\u5165URL\u5730\u5740"}),C==="upload"?(0,l.jsx)(H.Z,d()(d()({},Ee),{},{children:(0,l.jsx)(Q.Z,{style:{marginLeft:6},icon:(0,l.jsx)(Y.Z,{}),children:"\u70B9\u51FB\u4E0A\u4F20"})})):null]})]})}),te=ne},70412:function(j,i,e){"use strict";e.r(i);var m=e(30279),d=e.n(m),p=e(93236),U=e(86004),A=e(62086),f=U.Z.TextArea,y=(0,p.memo)(function(E){return(0,A.jsx)(f,d()({rows:6,placeholder:"\u8BF7\u8F93\u5165\u6D4B\u8BD5\u5185\u5BB9."},E))});i.default=y},87976:function(j,i,e){"use strict";var m=e(13183),d="http://ai.tbanx.cn",p=m.Z.create({baseURL:"".concat(d,"/api/"),headers:{Authorization:"senv2wk7w4jo93fn(um40lfdc!dycp#fcupm7^1ocdh6d@bn0t"}});i.Z=p},62938:function(){}}]);
