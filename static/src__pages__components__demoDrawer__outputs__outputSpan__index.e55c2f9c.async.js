(self.webpackChunkai_frontend=self.webpackChunkai_frontend||[]).push([[539,912],{43495:function(t,n,r){"use strict";r.r(n);var a=r(94434),l=r.n(a),o=r(93236),d=r(62464),u=r(38430),f=r(62086),_=(0,o.memo)(function(i){var e=i.data;if(console.log("data",e),e&&e.length){var p=(0,u.l)(e);return(0,f.jsx)(f.Fragment,{children:l()(p.values()).map(function(s,c){return(0,f.jsx)(d.default,{type:s.label,color:s.color,children:s.span},c)})})}return null});n.default=_},62464:function(t,n,r){"use strict";r.r(n),r.d(n,{default:function(){return u}});var a=r(93236),l={wrap:"wrap___kS59A"},o=r(62086),d=(0,a.memo)(function(f){var _=f.children,i=f.type,e=f.color;return i?(0,o.jsxs)("dl",{className:l.wrap,style:{backgroundColor:e==null?void 0:e.bgColor,borderColor:e==null?void 0:e.textColor},children:[(0,o.jsx)("dt",{children:_}),(0,o.jsx)("dd",{style:{color:e==null?void 0:e.textColor},children:i})]}):(0,o.jsx)("span",{children:_})}),u=d},38430:function(t,n,r){"use strict";r.d(n,{l:function(){return _}});var a=r(30279),l=r.n(a),o=r(94434),d=r.n(o),u=new Map([["blue",{textColor:"#5B8DFA",bgColor:"#EBF0FF"}],["purple",{textColor:"#9978F6",bgColor:"#EFE9FF"}],["cyan",{textColor:"#5DD5D1",bgColor:"#E5FCF7"}],["pink",{textColor:"#DD73F6",bgColor:"#FFE8FF"}],["yellow",{textColor:"#F9B847",bgColor:"#FFF6E3"}],["green",{textColor:"#5BD695",bgColor:"#EDFCF3"}],["red",{textColor:"#F26691",bgColor:"#FFECF0"}],["lime",{textColor:"#5b8c00",bgColor:"#fcffe6"}],["magenta",{textColor:"#9e1068",bgColor:"#fff0f6"}],["volcano",{textColor:"#d4380d",bgColor:"#fff2e8"}],["gold",{textColor:"#ad6800",bgColor:"#fffbe6"}],["geekblue",{textColor:"#10239e",bgColor:"#f0f5ff"}],["gray",{textColor:"#666666",bgColor:"#F5F5F5"}]]),f=d()(u.keys());function _(i){var e=arguments.length>1&&arguments[1]!==void 0?arguments[1]:"type";if(!i)return i;var p=new Map;return i.forEach(function(s){if(!s[e])throw new Error("genColorMap error: miss key: "+e+" in element");if(!p.has(s[e])){var c=p.size%f.length,C=f[c],y=u.get(C);p.set(s[e],l()(l()({},s),{},{color:y}))}}),p}},66618:function(t,n,r){"use strict";var a=r(93236),l=Symbol.for("react.element"),o=Symbol.for("react.fragment"),d=Object.prototype.hasOwnProperty,u=a.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner,f={key:!0,ref:!0,__self:!0,__source:!0};function _(i,e,p){var s,c={},C=null,y=null;p!==void 0&&(C=""+p),e.key!==void 0&&(C=""+e.key),e.ref!==void 0&&(y=e.ref);for(s in e)d.call(e,s)&&!f.hasOwnProperty(s)&&(c[s]=e[s]);if(i&&i.defaultProps)for(s in e=i.defaultProps,e)c[s]===void 0&&(c[s]=e[s]);return{$$typeof:l,type:i,key:C,ref:y,props:c,_owner:u.current}}n.Fragment=o,n.jsx=_,n.jsxs=_},62086:function(t,n,r){"use strict";t.exports=r(66618)},33737:function(t){function n(r,a){(a==null||a>r.length)&&(a=r.length);for(var l=0,o=new Array(a);l<a;l++)o[l]=r[l];return o}t.exports=n,t.exports.__esModule=!0,t.exports.default=t.exports},13989:function(t,n,r){var a=r(33737);function l(o){if(Array.isArray(o))return a(o)}t.exports=l,t.exports.__esModule=!0,t.exports.default=t.exports},56037:function(t){function n(r){if(typeof Symbol!="undefined"&&r[Symbol.iterator]!=null||r["@@iterator"]!=null)return Array.from(r)}t.exports=n,t.exports.__esModule=!0,t.exports.default=t.exports},90623:function(t){function n(){throw new TypeError(`Invalid attempt to spread non-iterable instance.
In order to be iterable, non-array objects must have a [Symbol.iterator]() method.`)}t.exports=n,t.exports.__esModule=!0,t.exports.default=t.exports},94434:function(t,n,r){var a=r(13989),l=r(56037),o=r(94945),d=r(90623);function u(f){return a(f)||l(f)||o(f)||d()}t.exports=u,t.exports.__esModule=!0,t.exports.default=t.exports},94945:function(t,n,r){var a=r(33737);function l(o,d){if(!!o){if(typeof o=="string")return a(o,d);var u=Object.prototype.toString.call(o).slice(8,-1);if(u==="Object"&&o.constructor&&(u=o.constructor.name),u==="Map"||u==="Set")return Array.from(o);if(u==="Arguments"||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(u))return a(o,d)}}t.exports=l,t.exports.__esModule=!0,t.exports.default=t.exports}}]);
