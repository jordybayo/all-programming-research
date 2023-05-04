import { Component, Input, OnInit } from '@angular/core';
import { DevicesService } from '../services/device.service';

@Component({
  selector: 'app-devices',
  templateUrl: './devices.component.html',
  styleUrls: ['./devices.component.scss']
})
export class DevicesComponent implements OnInit {

  @Input() deviceName : string;
  @Input() deviceStatus:string;
  @Input() indexOfDevice: number;
  @Input() id: number;

  constructor(private deviceService: DevicesService) { }

  ngOnInit() {
  }

  getStatus(){
    return this.deviceStatus;
  }


  getColor(){
    if(this.deviceStatus === 'allume'){
      return 'green';
    }else if(this.deviceStatus === 'eteint'){
      return 'red';
    }
  }

  onSwitchOn(){
    this.deviceService.switchOnOne(this.indexOfDevice);
  }

  onSwitchOff(){
    this.deviceService.switchOffOne(this.indexOfDevice);
  }
}
