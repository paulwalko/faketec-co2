$fn=25;
l=81;
w=55;
h=3;

difference() {
    cube([l,w,h]);
    
    translate([4.5,4.5,1.5])
        cylinder(h=1.502,r=4.25);
    translate([l - 4.5,4.5,1.5])
        cylinder(h=1.502,r=4.25);
    translate([4.5,w - 4.5,1.5])
        cylinder(h=1.502,r=4.25);
    translate([l - 4.5,w - 4.5,1.5])
        cylinder(h=1.501,r=4.25);
    
    translate([4.5,4.5,-0.001])
        cylinder(h=1.502,r=1.65);
    translate([l - 4.5,4.5,-0.001])
        cylinder(h=1.502,r=1.65);
    translate([4.5,w - 4.5,-0.001])
        cylinder(h=1.502,r=1.65);
    translate([l - 4.5,w - 4.5,-0.001])
        cylinder(h=1.502,r=1.65);
}