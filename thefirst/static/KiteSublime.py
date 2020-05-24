.lb-loader,
.lightbox {
  text-align: center;
  line-height: 0;
}
.lb-dataContainer:after,
.lb-outerContainer:after {
  content: '';
  clear: both;
}
html.lb-disable-scrolling {
  overflow: hidden;
  position: fixed;
  height: 100vh;
  width: 100vw;
}
.lightboxOverlay {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 9999;
  background-color: #000;
  filter: alpha(Opacity=80);
  opacity: 0.8;
  display: none;
}
.lightbox {
  position: absolute;
  left: 0;
  width: 100%;
  z-index: 10000;
  font-weight: 400;
}
.lightbox .lb-image {
  display: block;
  height: auto;
  max-width: inherit;
  max-height: none;
  border-radius: 3px;
  border: 4px solid #fff;
}
.lightbox a img {
  border: none;
}
.lb-outerContainer {
  position: relative;
  width: 250px;
  height: 250px;
  margin: 0 auto;
  border-radius: 4px;
  background-color: #fff;
}
.lb-loader,
.lb-nav {
  position: absolute;
  left: 0;
}
.lb-outerContainer:after {
  display: table;
}
.lb-loader {
  top: 43%;
  height: 25%;
  width: 100%;
}
.lb-cancel {
  display: block;
  width: 32px;
  height: 32px;
  margin: 0 auto;
  background: url(../images/loading.gif) no-repeat;
}
.lb-nav {
  top: 0;
  height: 100%;
  width: 100%;
  z-index: 10;
}
.lb-container > .nav {
  left: 0;
}
.lb-nav a {
  outline: 0;
  background-image: url(data:image/gif;base64,R0lGODlhAQABAPAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==);
}
.lb-next,
.lb-prev {
  height: 100%;
  cursor: pointer;
  display: block;
}
.lb-nav a.lb-prev {
  width: 34%;
  left: 0;
  float: left;
  background: url(../img/lightbox/prev.png) left 48% no-repeat;
  filter: alpha(Opacity=0);
  opacity: 0;
  -webkit-transition: opacity 0.6s;
  -moz-transition: opacity 0.6s;
  -o-transition: opacity 0.6s;
  transition: opacity 0.6s;
}
.lb-nav a.lb-prev:hover {
  filter: alpha(Opacity=100);
  opacity: 1;
}
.lb-nav a.lb-next {
  width: 64%;
  right: 0;
  float: right;
  background: url(../img/lightbox/next.png) right 48% no-repeat;
  filter: alpha(Opacity=0);
  opacity: 0;
  -webkit-transition: opacity 0.6s;
  -moz-transition: opacity 0.6s;
  -o-transition: opacity 0.6s;
  transition: opacity 0.6s;
}
.lb-nav a.lb-next:hover {
  filter: alpha(Opacity=100);
  opacity: 1;
}
.lb-dataContainer {
  margin: 0 auto;
  padding-top: 5px;
  width: 100%;
  border-bottom-left-radius: 4px;
  border-bottom-right-radius: 4px;
}
.lb-dataContainer:after {
  display: table;
}
.lb-data {
  padding: 0 4px;
  color: #ccc;
}
.lb-data .lb-details {
  width: 85%;
  float: left;
  text-align: left;
  line-height: 1.1em;
}
.lb-data .lb-caption {
  font-size: 13px;
  font-weight: 700;
  line-height: 1em;
}
.lb-data .lb-caption a {
  color: #4ae;
}
.lb-data .lb-number {
  display: block;
  clear: left;
  padding-bottom: 1em;
  font-size: 12px;
  color: #999;
}
.lb-data .lb-close {
  display: block;
  float: right;
  width: 30px;
  height: 30px;
  background: url(../img/lightbox/close.png) top right no-repeat;
  text-align: right;
  outline: 0;
  filter: alpha(Opacity=70);
  opacity: 0.7;
  -webkit-transition: opacity 0.2s;
  -moz-transition: opacity 0.2s;
  -o-transition: opacity 0.2s;
  transition: opacity 0.2s;
}
.lb-data .lb-close:hover {
  cursor: pointer;
  filter: alpha(Opacity=100);
  opacity: 1;
}
