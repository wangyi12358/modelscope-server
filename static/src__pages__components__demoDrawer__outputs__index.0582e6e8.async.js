(self.webpackChunkai_frontend=self.webpackChunkai_frontend||[]).push([[773,382],{96297:function(r,e,t){"use strict";t.r(e);var n=t(43495),a=t(89347),o=t(39801),s=t(50726),u={spans:n.default,scores:a.default,text:o.default,texts:o.default,imageUrl:s.default};e.default=u},50726:function(r,e,t){"use strict";t.r(e),t.d(e,{default:function(){return d}});var n=t(93236),a=t(41385),o={imageBox:"imageBox___kwPcl"},s=t(62086),u=(0,n.memo)(function(f){return(0,s.jsx)("div",{className:o.imageBox,children:(0,s.jsx)(a.Z,{src:f.data,preview:!0})})}),d=u},89347:function(r,e,t){"use strict";t.r(e);var n=t(93236),a=t(11557),o=t(62086),s=(0,n.memo)(function(u){return u.data?(0,o.jsx)(a.Z,{pagination:!1,bordered:!0,dataSource:u.data,rowKey:"label",columns:[{dataIndex:"label",title:"\u9884\u6D4B\u7ED3\u679C"},{dataIndex:"score",title:"\u9884\u6D4B\u6982\u7387(\u53EF\u4FE1\u5EA6)"}]}):null});e.default=s},43495:function(r,e,t){"use strict";t.r(e);var n=t(94434),a=t.n(n),o=t(93236),s=t(62464),u=t(38430),d=t(62086),f=(0,o.memo)(function(i){var l=i.data;if(console.log("data",l),l&&l.length){var c=(0,u.l)(l);return(0,d.jsx)(d.Fragment,{children:a()(c.values()).map(function(v,x){return(0,d.jsx)(s.default,{type:v.label,color:v.color,children:v.span},x)})})}return null});e.default=f},62464:function(r,e,t){"use strict";t.r(e),t.d(e,{default:function(){return u}});var n=t(93236),a={wrap:"wrap___kS59A"},o=t(62086),s=(0,n.memo)(function(d){var f=d.children,i=d.type,l=d.color;return i?(0,o.jsxs)("dl",{className:a.wrap,style:{backgroundColor:l==null?void 0:l.bgColor,borderColor:l==null?void 0:l.textColor},children:[(0,o.jsx)("dt",{children:f}),(0,o.jsx)("dd",{style:{color:l==null?void 0:l.textColor},children:i})]}):(0,o.jsx)("span",{children:f})}),u=s},39801:function(r,e,t){"use strict";t.r(e),t.d(e,{default:function(){return u}});var n=t(93236),a={list:"list___xeNje",item:"item___k2KDK"},o=t(62086),s=(0,n.memo)(function(d){var f=d.data;if(!f)return null;var i=[].concat(f);return(0,o.jsx)("div",{className:a.list,children:i.map(function(l,c){return(0,o.jsx)("div",{className:a.item,children:l},c)})})}),u=s},38430:function(r,e,t){"use strict";t.d(e,{l:function(){return f}});var n=t(30279),a=t.n(n),o=t(94434),s=t.n(o),u=new Map([["blue",{textColor:"#5B8DFA",bgColor:"#EBF0FF"}],["purple",{textColor:"#9978F6",bgColor:"#EFE9FF"}],["cyan",{textColor:"#5DD5D1",bgColor:"#E5FCF7"}],["pink",{textColor:"#DD73F6",bgColor:"#FFE8FF"}],["yellow",{textColor:"#F9B847",bgColor:"#FFF6E3"}],["green",{textColor:"#5BD695",bgColor:"#EDFCF3"}],["red",{textColor:"#F26691",bgColor:"#FFECF0"}],["lime",{textColor:"#5b8c00",bgColor:"#fcffe6"}],["magenta",{textColor:"#9e1068",bgColor:"#fff0f6"}],["volcano",{textColor:"#d4380d",bgColor:"#fff2e8"}],["gold",{textColor:"#ad6800",bgColor:"#fffbe6"}],["geekblue",{textColor:"#10239e",bgColor:"#f0f5ff"}],["gray",{textColor:"#666666",bgColor:"#F5F5F5"}]]),d=s()(u.keys());function f(i){var l=arguments.length>1&&arguments[1]!==void 0?arguments[1]:"type";if(!i)return i;var c=new Map;return i.forEach(function(v){if(!v[l])throw new Error("genColorMap error: miss key: "+l+" in element");if(!c.has(v[l])){var x=c.size%d.length,C=d[x],p=u.get(C);c.set(v[l],a()(a()({},v),{},{color:p}))}}),c}},33737:function(r){function e(t,n){(n==null||n>t.length)&&(n=t.length);for(var a=0,o=new Array(n);a<n;a++)o[a]=t[a];return o}r.exports=e,r.exports.__esModule=!0,r.exports.default=r.exports},13989:function(r,e,t){var n=t(33737);function a(o){if(Array.isArray(o))return n(o)}r.exports=a,r.exports.__esModule=!0,r.exports.default=r.exports},56037:function(r){function e(t){if(typeof Symbol!="undefined"&&t[Symbol.iterator]!=null||t["@@iterator"]!=null)return Array.from(t)}r.exports=e,r.exports.__esModule=!0,r.exports.default=r.exports},90623:function(r){function e(){throw new TypeError(`Invalid attempt to spread non-iterable instance.
In order to be iterable, non-array objects must have a [Symbol.iterator]() method.`)}r.exports=e,r.exports.__esModule=!0,r.exports.default=r.exports},94434:function(r,e,t){var n=t(13989),a=t(56037),o=t(94945),s=t(90623);function u(d){return n(d)||a(d)||o(d)||s()}r.exports=u,r.exports.__esModule=!0,r.exports.default=r.exports},94945:function(r,e,t){var n=t(33737);function a(o,s){if(!!o){if(typeof o=="string")return n(o,s);var u=Object.prototype.toString.call(o).slice(8,-1);if(u==="Object"&&o.constructor&&(u=o.constructor.name),u==="Map"||u==="Set")return Array.from(o);if(u==="Arguments"||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(u))return n(o,s)}}r.exports=a,r.exports.__esModule=!0,r.exports.default=r.exports}}]);
