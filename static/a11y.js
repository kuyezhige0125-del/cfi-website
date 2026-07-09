// CFI Accessibility Controls
(function(){
function changeFontSize(d){var c=parseInt(localStorage.getItem("cfi-fs")||"1");c=Math.max(1,Math.min(3,c+d));document.documentElement.dataset.fontSize=c;localStorage.setItem("cfi-fs",c)}
function toggleHC(){var c=document.documentElement.dataset.highContrast!=="true";document.documentElement.dataset.highContrast=c;localStorage.setItem("cfi-hc",c)}
function toggleMenu(){document.querySelector(".nav-links").classList.toggle("open")}
document.addEventListener("DOMContentLoaded",function(){var fs=localStorage.getItem("cfi-fs")||"1";document.documentElement.dataset.fontSize=fs;var hc=localStorage.getItem("cfi-hc")==="true";document.documentElement.dataset.highContrast=hc})
document.querySelector(".hamburger")&&document.querySelector(".hamburger").addEventListener("click",toggleMenu)
// Expose for inline onclick usage
window.changeFontSize=changeFontSize;window.toggleHC=toggleHC;window.toggleMenu=toggleMenu
})()