"use strict";(self.webpackChunkai_frontend=self.webpackChunkai_frontend||[]).push([[858,800],{6241:function(R,M,n){n.d(M,{ay:function(){return c},gb:function(){return I}});var P=n(30279),d=n.n(P),r=n(93236),f=n(32699),N=n.n(f),O=n(38430),g=n(86741),A=n(86504),S=n(92499),m=n(62086),t={current:{domains:{nlp:{name:"\u81EA\u7136\u8BED\u8A00\u5904\u7406",fullName:"Natural Language Processing",tasks:[]},cv:{name:"\u8BA1\u7B97\u673A\u89C6\u89C9",fullName:"Computer Vision",tasks:[]},multiModal:{name:"\u591A\u6A21\u6001",fullName:"Multi-Modal",tasks:[]}}}};function o(i){t.current=i}function h(){return t.current}var j=r.createContext(null),B={nlp:(0,m.jsx)(g.Z,{}),cv:(0,m.jsx)(A.Z,{}),multiModal:(0,m.jsx)(S.Z,{})},I=function(D){var x=D.children,l=D.domains,T=c(),u=(0,r.useMemo)(function(){if(l)return(0,O.l)(Object.keys(l).map(function(s){return d()({type:s,icon:B[s]},l==null?void 0:l[s])}))},[l]),p=(0,r.useMemo)(function(){var s=[];return l&&Object.keys(l).map(function(a){var C=u==null?void 0:u.get(a);C.tasks.forEach(function(e){var v;e!=null&&(v=e.models)!==null&&v!==void 0&&v.length&&(s=s.concat(e==null?void 0:e.models.map(function(E){return d()(d()({},E),{},{task:(0,f.omit)(e,"models"),domain:(0,f.omit)(C,"tasks")})})))})}),s},[l,u]);return(0,m.jsx)(j.Provider,{value:d()(d()({},T),{},{domains:l,models:p,domainsMap:u}),children:x})};function c(){var i;return(i=(0,r.useContext)(j))!==null&&i!==void 0?i:h()}},53145:function(R,M,n){n.r(M),n.d(M,{default:function(){return B}});var P=n(46686),d=n.n(P),r=n(93236),f=n(8195),N=n(8942),O=n(46859),g=n(66122),A=n(65348),S=n(13924),m=n(6241),t={list:"list___JH7iC",card:"card___ZgVDF",line:"line___SuZOP",info:"info___bbqpm",desc:"desc___WuK3G",operation:"operation___NOIJv"},o=n(62086),h=f.Z.Title;function j(){var I=(0,m.ay)(),c=I.models,i=(0,r.useState)(),D=d()(i,2),x=D[0],l=D[1],T=(0,r.useState)(!1),u=d()(T,2),p=u[0],s=u[1];return(0,o.jsxs)("div",{children:[(0,o.jsx)(h,{level:4,children:"\u53EF\u7528\u6A21\u578B\u529F\u80FD\u6F14\u793A"}),(0,o.jsx)("div",{className:t.list,children:c==null?void 0:c.map(function(a,C){var e,v,E,K,_=a==null||(e=a.domain)===null||e===void 0?void 0:e.color;return(0,o.jsx)(N.Z,{children:(0,o.jsxs)("div",{className:t.card,children:[(0,o.jsx)("div",{className:t.line,style:{backgroundColor:_==null?void 0:_.bgColor}}),(0,o.jsxs)("div",{className:t.info,children:[(0,o.jsxs)(h,{level:5,children:[(0,o.jsx)("span",{style:{color:_==null?void 0:_.textColor},children:a==null||(v=a.domain)===null||v===void 0?void 0:v.icon})," ",a.name," ",(0,o.jsx)(O.Z,{children:(E=a.languages)===null||E===void 0?void 0:E.map(function(L){return(0,o.jsx)(A.Z,{lang:L},L)})})]}),(0,o.jsx)("div",{className:t.desc,children:a==null||(K=a.task)===null||K===void 0?void 0:K.desc})]}),(0,o.jsx)("div",{className:t.operation,children:(0,o.jsx)(g.Z,{size:"small",onClick:function(){l(a),s(!0)},children:"\u70B9\u51FB\u4F53\u9A8C"})})]})},C)})}),x&&(0,o.jsx)(S.default,{model:x,open:p,onClose:function(){s(!1)}})]})}var B=j}}]);