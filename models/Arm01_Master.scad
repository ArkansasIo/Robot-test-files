// ARM01 master conceptual OpenSCAD model. Units: mm.
// Final structural, actuator, bearing and safety engineering is required before fabrication.
$fn = 48;
upper_len=400;
fore_len=400;
extension_len=400;
plate_t=8;
link_w=55;
joint_r=35;
base_w=180;
base_d=180;

module plate(len,w,t=plate_t){ translate([0,-w/2,0]) cube([len,w,t]); }
module joint(r=35,t=plate_t){ cylinder(h=t,r=r); }
module arm01(){
  cube([base_w,base_d,plate_t],center=true);
  translate([0,0,40]) rotate([0,90,0]) joint();
  translate([joint_r,0,40]) plate(upper_len,link_w);
  translate([joint_r+upper_len,0,40]) joint(30);
  translate([joint_r+upper_len+25,0,40]) plate(fore_len,link_w);
  translate([joint_r+upper_len+fore_len+5,0,42]) cube([extension_len,35,12]);
  translate([joint_r+upper_len+fore_len+extension_len+5,0,42]) joint(22);
}
arm01();

// Uncomment for a conceptual 12-module radial arrangement:
// for(i=[0:11]) rotate([0,0,i*30]) translate([250,0,0]) arm01();
