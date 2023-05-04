import { Component, OnInit } from '@angular/core';
import { DevicesService } from '../services/device.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-device-view',
  templateUrl: './device-view.component.html',
  styleUrls: ['./device-view.component.scss']
})
export class DeviceViewComponent implements OnInit {

  isAuth = false;

  lastUpdate = new Promise(
    (resolve, reject)=>{
      const date = Date();
      setTimeout(
        ()=>{resolve(date);},
        2000
      );
    }
  );

  devices: any[];
  deviceSubscription: Subscription;

  constructor(private deviceService:DevicesService){

    setTimeout(
      ()=>{this.isAuth = true;}, 
      4000
    );

  }

  ngOnInit(){
    this.deviceSubscription = this.deviceService.deviceSubject.subscribe(
      (devices: any[])=>{
        this.devices = devices;
      });
    this.deviceService.emitDeviceSubject();
  }

  onAllumer(){
    this.deviceService.switchOnAll();
  }

  onEteindre(){
     this.deviceService.switchOffAll();
  }

}
