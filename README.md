### Coordinate system

- x,y horizontal plane
- z vertical axis

### Links

- https://keisan.casio.com/exec/system/1359533867

### Msgs

- Vector3
- Spherical

### Sensors

- IMU

```
entity_name: "box::base_link::imu_sensor"
orientation {
  x: 3.3912276258161742e-06
  y: -1.4904375319275085e-06
  z: 0.91547946881208253
  w: 0.40236468802545938
}
angular_velocity {
  x: 6.1738317922930516e-06
  y: 7.6839963575482e-11
  z: 0.83333333427623846
}
linear_acceleration {
  x: 0.34738135829879818
  y: 0.068983587197537707
  z: 9.7999974270287655
}
```

### Getting Started

- cd <working_directory>
- python3 -m venv env
- source env/bin/activate
- pip3 install -r requirements.txt
