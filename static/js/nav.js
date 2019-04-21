var sidenav = new Sidenav("sidenav");
  document.getElementById("sidenav").addEventListener("click", function () {
  sidenav.openClose();
})

function Sidenav(ob) {
  var navId = (ob !== null && typeof ob === 'object') ? ob.id : ob;
  var opt = ob || {};

  this.isOpen = opt.isOpen || false;
  this.sidenav = document.getElementById(navId);
}

// True is open, false is close and no option is toggle
Sidenav.prototype.openClose = function (open) {
  var self = this;
  self.isOpen = open || !self.isOpen;
  if (self.isOpen) {
      self.sidenav.classList.add("open");
  } else {
      self.sidenav.classList.remove("open");
  }
}