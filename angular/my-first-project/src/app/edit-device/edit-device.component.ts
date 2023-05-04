import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { DevicesService } from '../services/device.service';

@Component({
  selector: 'app-edit-device',
  templateUrl: './edit-device.component.html',
  styleUrls: ['./edit-device.component.scss']
})
export class EditDeviceComponent implements OnInit {

  defaultOnOff = "eteint";

  constructor(private deviceServices: DevicesService,
              private router: Router) { }

  ngOnInit() {
  }

  onSubmit(form: NgForm){
    const name = form.value['name'];
    const status = form.value['status'];
    this.deviceServices.addDevice(name, status);
    this.router.navigate(['/devices']);
  }

}
