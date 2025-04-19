$fn=25;
l=81;
w=55;
h=25;
wl=3;
difference() {
    union(){
        difference() {
            cube([l,w,h]);
            translate([wl,wl,wl + 0.001])
                cube([l - wl * 2, w - wl * 2, h - wl]);
        }
        
        // co2 vent
        translate([27,11,3])
            cube([15,15,3]);
        
        // board screws
        translate([50,4.5,3])
            cylinder(h=9,r=2);
        translate([50,26.5,3])
            cylinder(h=9,r=2);
    }
    
    // co2 vent pt 1
    translate([28,12,1])
        cube([13,13,6]);
    
    // co2 vent pt 2
    translate([30.5,14.5,-0.001])
        cylinder(h=1.002,r=1.5);
    translate([34.5,14.5,-0.001])
        cylinder(h=1.002,r=1.5);
    translate([38.5,14.5,-0.001])
        cylinder(h=1.002,r=1.5);
    translate([30.5,18.5,-0.001])
        cylinder(h=1.002,r=1.5);
    translate([34.5,18.5,-0.001])
        cylinder(h=1.002,r=1.5);
    translate([38.5,18.5,-0.001])
        cylinder(h=1.002,r=1.5);
    translate([30.5,22.5,-0.001])
        cylinder(h=1.002,r=1.5);
    translate([34.5,22.5,-0.001])
        cylinder(h=1.002,r=1.5);
    translate([38.5,22.5,-0.001])
        cylinder(h=1.002,r=1.5);
    
    // usb c
    translate([-0.001,8,13.001])
        cube([2,16,12]);
        
    translate([-0.001,11,16.001])
        cube([3.002,10,7]);
        
    // board screws
    translate([50,4.6,7])
        cylinder(h=5.001,r=1);
        
    translate([50,26.5,7])
        cylinder(h=5.001,r=1);

    // antenna
    translate([l - 7,1.5,11])
    rotate([0,90,90])
        cylinder(r=4.75, h=1.501, $fn=6);
    translate([l - 7,-0.001,11])
    rotate([0,90,90])
        cylinder(r=3.25, h=1.502);
        
    // switch
    translate([40,-0.001,h - 6 + 0.001])
        cube([11,3.002,6]);
    translate([38,-0.001,h - 6 + 3])
    rotate([0,90,90])
        cylinder(r=1.25,h=3.002);
    translate([53,-0.001,h - 6 + 3])
    rotate([0,90,90])
        cylinder(r=1.25,h=3.002);
}

// pcb stabilizer
translate([3,3,10])
    cube([2,2,2]);
translate([3,3,14])
    cube([2,2,2]);
translate([3,25,10])
    cube([2,2,2]);
translate([3,25,14])
    cube([2,2,2]);

// lid screws
difference() {
    union () {
        translate([4.5,4.5,22])
            cylinder(h=3,r=3);
        translate([l - 4.5,4.5,22])
            cylinder(h=3,r=3);
        translate([4.5,w - 4.5,22])
            cylinder(h=3,r=3);
        translate([l - 4.5,w - 4.5,22])
            cylinder(h=3,r=3);
    }
    
    translate([4.5,4.5,22 - 0.001])
        cylinder(h=3.002,r=1.65);
    
    translate([l - 4.5,4.5,22 - 0.001])
        cylinder(h=3.002,r=1.65);
    
    translate([4.5,w - 4.5,22 - 0.001])
        cylinder(h=3.002,r=1.65);
    
    translate([l - 4.5,w - 4.5,22 - 0.001])
        cylinder(h=3.002,r=1.65);
}