(self.webpackChunkai_frontend=self.webpackChunkai_frontend||[]).push([[699,382,214],{65348:function(F,t,n){"use strict";n.d(t,{Z:function(){return h}});var i=n(93236),u=n(38430),e={langBadge:"langBadge___GAdAy"},m=n(62086),v=[{lang:"en_US",name:"EN"},{lang:"zh_CN",name:"\u4E2D\u6587"}],l=(0,u.l)(v,"lang"),E=function(p){var s=l.get(p.lang);return(0,m.jsx)("span",{className:e.langBadge,style:{backgroundColor:s.color.textColor},children:s.name})},h=E},440:function(F,t,n){"use strict";n.r(t),n.d(t,{default:function(){return Y}});var i=n(30279),u=n.n(i),e=n(46686),m=n.n(e),v=n(35290),l=n.n(v),E=n(411),h=n.n(E),a=n(93236),p=n(8195),s=n(35768),S=n(66122),W=n(24381),I=n(46859),N=n(54418),q=n(96297),_=n(87976),nn=n(36752),tn=n(74524),en={footer:"footer___CvaU9"},G=n(82137),an=n(65348),o=n(62086),z=p.Z.Title,rn=(0,a.memo)(function(D){var V,r=D.model,L=D.open,Z=D.onClose,P=function(){var g=h()(l()().mark(function x(U){return l()().wrap(function(M){for(;;)switch(M.prev=M.next){case 0:return M.abrupt("return",_.Z.post(r.apiPath,U));case 1:case"end":return M.stop()}},x)}));return function(U){return g.apply(this,arguments)}}(),H=s.Z.useForm(),un=m()(H,1),A=un[0],d=(r==null?void 0:r.samples)&&r.samples.length>0,K=(0,G.Z)(P,{manual:!0}),$=K.loading,y=K.data,O=K.run,X=K.mutate,Q=(0,a.useCallback)(function(){if(d){var g=(0,nn.ei)(r.samples);A.setFieldValue("inputContent",g)}},[A,d,r]),b=function(){return d?(0,o.jsx)(S.Z,{size:"small",disabled:$,onClick:Q,icon:(0,o.jsx)(tn.Z,{}),children:"\u66F4\u6362\u793A\u4F8B"}):null},w=(0,a.useMemo)(function(){var g=null;if(r!=null&&r.input){var x=N.default[r.input];x?g=(0,o.jsx)(s.Z.Item,{name:"inputContent",rules:[{required:!0,message:"\u8BF7\u8F93\u5165\u6D4B\u8BD5\u5185\u5BB9!"}],children:(0,o.jsx)(x,{})}):g=(0,o.jsxs)("div",{children:["\u6682\u65E0\u6B64\u7C7B\u578B\u8F93\u5165\u6A21\u5757 : ",(0,o.jsx)("strong",{children:r.input})]})}return g},[r]),J=(0,a.useMemo)(function(){var g,x=null;if(y&&y!==null&&y!==void 0&&(g=y.data)!==null&&g!==void 0&&g.data){var U,k=y==null||(U=y.data)===null||U===void 0?void 0:U.data;if(r!=null&&r.output){var M=q.default[r.output];M?x=(0,o.jsx)(M,{data:k}):x=(0,o.jsxs)("div",{children:["\u6682\u65E0\u6B64\u7C7B\u578B\u8F93\u51FA\u6A21\u5757 : ",(0,o.jsx)("strong",{children:r.output})]})}return(0,o.jsxs)(o.Fragment,{children:[(0,o.jsx)(z,{level:5,children:"\u6D4B\u8BD5\u7ED3\u679C:"}),x]})}return null},[y,r]),ln=function(x){O(u()({},x))};return(0,a.useEffect)(function(){d&&A.setFieldValue("inputContent",r==null?void 0:r.samples[0])},[A,d,r==null?void 0:r.samples]),r?(0,o.jsx)(W.Z,{afterOpenChange:function(x){x?Q():(A.resetFields(),X(void 0))},destroyOnClose:!0,open:L,onClose:Z,width:"60%",footer:(0,o.jsx)("div",{className:en.footer,children:(0,o.jsxs)(I.Z,{size:24,children:[(0,o.jsx)(S.Z,{onClick:Z,children:"\u5173\u95ED"}),(0,o.jsx)(S.Z,{type:"primary",onClick:function(){return A.submit()},loading:$,children:"\u63D0\u4EA4\u6D4B\u8BD5"})]})}),children:(0,o.jsxs)("div",{children:[(0,o.jsxs)(z,{level:5,style:{display:"flex",justifyContent:"space-between"},children:[(0,o.jsxs)("span",{children:[r.name," \u6D4B\u8BD5\u5185\u5BB9 "," ",(0,o.jsx)(I.Z,{children:(V=r.languages)===null||V===void 0?void 0:V.map(function(g){return(0,o.jsx)(an.Z,{lang:g},g)})})]}),b()]}),(0,o.jsx)(s.Z,{layout:"vertical",form:A,onFinish:ln,children:w}),(0,o.jsx)("div",{children:$?(0,o.jsx)(z,{level:5,children:"\u6D4B\u8BD5\u7ED3\u679C\u751F\u6210\u4E2D, \u8BF7\u7A0D\u7B49..."}):J})]})}):null}),Y=rn},54418:function(F,t,n){"use strict";n.r(t);var i=n(70412),u=n(47682),e={text:i.default,imageUrl:u.default,videoUrl:u.default};t.default=e},47682:function(F,t,n){"use strict";n.r(t),n.d(t,{default:function(){return r}});var i=n(30279),u=n.n(i),e=n(94434),m=n.n(e),v=n(35290),l=n.n(v),E=n(411),h=n.n(E),a=n(46686),p=n.n(a),s=n(93236),S=n(65713),W=n(41385),I=n(86004),N=n(929),q=n(17986),_=n(66122),nn=n(61654),tn=n(87976);function en(){return G.apply(this,arguments)}function G(){return G=h()(l()().mark(function L(){return l()().wrap(function(P){for(;;)switch(P.prev=P.next){case 0:return P.abrupt("return",tn.Z.get("oss/sign"));case 1:case"end":return P.stop()}},L)})),G.apply(this,arguments)}var an=n(47277),o=n(12383),z=n(17771),rn={preview:"preview___Rqv6O"},Y=n(32699),D=n(62086),V=(0,s.memo)(function(L){var Z=L.value,P=L.onChange,H=P===void 0?function(){}:P,un=(0,s.useState)(),A=p()(un,2),d=A[0],K=A[1],$=(0,s.useState)(Z),y=p()($,2),O=y[0],X=y[1],Q=(0,s.useState)(null),b=p()(Q,2),w=b[0],J=b[1],ln=(0,s.useState)("url"),g=p()(ln,2),x=g[0],U=g[1],k=(0,s.useState)([]),M=p()(k,2),T=M[0],sn=M[1],fn=(0,z.A)({sources:[{src:O}]}),mn=fn.Video,cn=(0,an.Z)(H,{wait:300}),dn=cn.run;(0,o.Z)(function(){X(Z)},[Z]);var vn=function(){var c=h()(l()().mark(function f(){var C,j;return l()().wrap(function(B){for(;;)switch(B.prev=B.next){case 0:return B.prev=0,B.next=3,en();case 3:j=B.sent,K(j==null||(C=j.data)===null||C===void 0?void 0:C.data),B.next=11;break;case 7:B.prev=7,B.t0=B.catch(0),console.error(B.t0),S.ZP.error("\u4E0A\u4F20\u5931\u8D25,\u8BF7\u7A0D\u540E\u91CD\u8BD5");case 11:case"end":return B.stop()}},f,null,[[0,7]])}));return function(){return c.apply(this,arguments)}}();(0,s.useEffect)(function(){x==="upload"&&vn()},[x]),(0,s.useEffect)(function(){if(T&&T.length){var c=T==null?void 0:T[0];if((c==null?void 0:c.percent)===100){var f,C;X((d==null?void 0:d.host)+"/"+(c==null?void 0:c.url));var j=null;c!=null&&(f=c.type)!==null&&f!==void 0&&f.startsWith("image")&&(j="image"),c!=null&&(C=c.type)!==null&&C!==void 0&&C.startsWith("video")&&(j="video"),J(j)}}},[d,T,H]);var gn=function(f){var C=f.fileList,j=C===void 0?[]:C;sn(m()(j))},hn=function(f){var C=(T||[]).filter(function(j){return j.url!==f.url});sn(C)},Cn=function(f){return{key:f.url,OSSAccessKeyId:d==null?void 0:d.OSSAccessKeyId,policy:d==null?void 0:d.policy,Signature:d==null?void 0:d.Signature}},En=function(){var c=h()(l()().mark(function f(C){var j,on,B;return l()().wrap(function(R){for(;;)switch(R.prev=R.next){case 0:if(d){R.next=2;break}return R.abrupt("return",!1);case 2:if(j=Number(d.expire)*1e3,!(j<Date.now())){R.next=6;break}return R.next=6,vn();case 6:return on=C.name.slice(C.name.lastIndexOf(".")),B=Date.now()+on,C.url=d.dir+"/"+B,R.abrupt("return",C);case 10:case"end":return R.stop()}},f)}));return function(C){return c.apply(this,arguments)}}(),xn={name:"file",fileList:T,multiple:!1,maxCount:1,accept:"video/*, image/*",action:d==null?void 0:d.host,onChange:gn,onRemove:hn,data:Cn,beforeUpload:En},pn=function(f){var C=f.target.value;X(C)};(0,s.useEffect)(function(){O&&((0,Y.endsWith)(".mp4",O)&&J("image"),(0,Y.endsWith)(".jpg",O)&&J("image"),dn(O))},[dn,O]);var Dn=function(){var f=null;return O&&w==="image"&&(f=(0,D.jsx)("div",{className:rn.preview,children:(0,D.jsx)(W.Z,{src:O})})),O&&w==="video"&&(f=(0,D.jsx)(mn,{width:400,src:O})),f};return(0,D.jsxs)("div",{children:[Dn(),(0,D.jsxs)(I.Z.Group,{compact:!0,children:[(0,D.jsxs)(N.Z,{value:x,onChange:function(f){return U(f)},children:[(0,D.jsx)(N.Z.Option,{value:"url",children:"\u8F93\u5165URL"}),(0,D.jsx)(N.Z.Option,{value:"upload",children:"\u672C\u5730\u4E0A\u4F20"})]}),(0,D.jsx)(I.Z,{value:O,onChange:pn,disabled:x==="upload",style:{width:"70%"},placeholder:"\u8BF7\u8F93\u5165URL\u5730\u5740"}),x==="upload"?(0,D.jsx)(q.Z,u()(u()({},xn),{},{children:(0,D.jsx)(_.Z,{style:{marginLeft:6},icon:(0,D.jsx)(nn.Z,{}),children:"\u70B9\u51FB\u4E0A\u4F20"})})):null]})]})}),r=V},70412:function(F,t,n){"use strict";n.r(t);var i=n(30279),u=n.n(i),e=n(93236),m=n(86004),v=n(62086),l=m.Z.TextArea,E=(0,e.memo)(function(h){return(0,v.jsx)(l,u()({rows:6,placeholder:"\u8BF7\u8F93\u5165\u6D4B\u8BD5\u5185\u5BB9."},h))});t.default=E},96297:function(F,t,n){"use strict";n.r(t);var i=n(43495),u=n(89347),e=n(39801),m=n(50726),v={spans:i.default,scores:u.default,text:e.default,texts:e.default,imageUrl:m.default};t.default=v},50726:function(F,t,n){"use strict";n.r(t),n.d(t,{default:function(){return l}});var i=n(93236),u=n(41385),e={imageBox:"imageBox___kwPcl"},m=n(62086),v=(0,i.memo)(function(E){return(0,m.jsx)("div",{className:e.imageBox,children:(0,m.jsx)(u.Z,{src:E.data,preview:!0})})}),l=v},89347:function(F,t,n){"use strict";n.r(t);var i=n(93236),u=n(11557),e=n(62086),m=(0,i.memo)(function(v){return v.data?(0,e.jsx)(u.Z,{pagination:!1,bordered:!0,dataSource:v.data,rowKey:"label",columns:[{dataIndex:"label",title:"\u9884\u6D4B\u7ED3\u679C"},{dataIndex:"score",title:"\u9884\u6D4B\u6982\u7387(\u53EF\u4FE1\u5EA6)"}]}):null});t.default=m},43495:function(F,t,n){"use strict";n.r(t);var i=n(94434),u=n.n(i),e=n(93236),m=n(62464),v=n(38430),l=n(62086),E=(0,e.memo)(function(h){var a=h.data;if(console.log("data",a),a&&a.length){var p=(0,v.l)(a);return(0,l.jsx)(l.Fragment,{children:u()(p.values()).map(function(s,S){return(0,l.jsx)(m.default,{type:s.label,color:s.color,children:s.span},S)})})}return null});t.default=E},62464:function(F,t,n){"use strict";n.r(t),n.d(t,{default:function(){return v}});var i=n(93236),u={wrap:"wrap___kS59A"},e=n(62086),m=(0,i.memo)(function(l){var E=l.children,h=l.type,a=l.color;return h?(0,e.jsxs)("dl",{className:u.wrap,style:{backgroundColor:a==null?void 0:a.bgColor,borderColor:a==null?void 0:a.textColor},children:[(0,e.jsx)("dt",{children:E}),(0,e.jsx)("dd",{style:{color:a==null?void 0:a.textColor},children:h})]}):(0,e.jsx)("span",{children:E})}),v=m},39801:function(F,t,n){"use strict";n.r(t),n.d(t,{default:function(){return v}});var i=n(93236),u={list:"list___xeNje",item:"item___k2KDK"},e=n(62086),m=(0,i.memo)(function(l){var E=l.data;if(!E)return null;var h=[].concat(E);return(0,e.jsx)("div",{className:u.list,children:h.map(function(a,p){return(0,e.jsx)("div",{className:u.item,children:a},p)})})}),v=m},38430:function(F,t,n){"use strict";n.d(t,{l:function(){return E}});var i=n(30279),u=n.n(i),e=n(94434),m=n.n(e),v=new Map([["blue",{textColor:"#5B8DFA",bgColor:"#EBF0FF"}],["purple",{textColor:"#9978F6",bgColor:"#EFE9FF"}],["cyan",{textColor:"#5DD5D1",bgColor:"#E5FCF7"}],["pink",{textColor:"#DD73F6",bgColor:"#FFE8FF"}],["yellow",{textColor:"#F9B847",bgColor:"#FFF6E3"}],["green",{textColor:"#5BD695",bgColor:"#EDFCF3"}],["red",{textColor:"#F26691",bgColor:"#FFECF0"}],["lime",{textColor:"#5b8c00",bgColor:"#fcffe6"}],["magenta",{textColor:"#9e1068",bgColor:"#fff0f6"}],["volcano",{textColor:"#d4380d",bgColor:"#fff2e8"}],["gold",{textColor:"#ad6800",bgColor:"#fffbe6"}],["geekblue",{textColor:"#10239e",bgColor:"#f0f5ff"}],["gray",{textColor:"#666666",bgColor:"#F5F5F5"}]]),l=m()(v.keys());function E(h){var a=arguments.length>1&&arguments[1]!==void 0?arguments[1]:"type";if(!h)return h;var p=new Map;return h.forEach(function(s){if(!s[a])throw new Error("genColorMap error: miss key: "+a+" in element");if(!p.has(s[a])){var S=p.size%l.length,W=l[S],I=v.get(W);p.set(s[a],u()(u()({},s),{},{color:I}))}}),p}},87976:function(F,t,n){"use strict";var i=n(13183),u="http://ai.tbanx.cn",e=i.Z.create({baseURL:"".concat(u,"/api/"),headers:{Authorization:"senv2wk7w4jo93fn(um40lfdc!dycp#fcupm7^1ocdh6d@bn0t"}});t.Z=e},62938:function(){}}]);