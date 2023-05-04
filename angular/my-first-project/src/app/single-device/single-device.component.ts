import { Component, OnInit } from '@angular/core';
import { DevicesService } from '../services/device.service';
import { ActivatedRoute } from '@angular/router';


@Component({
  selector: 'app-single-device',
  templateUrl: './single-device.component.html',
  styleUrls: ['./single-device.component.scss']
})
export class SingleDeviceComponent implements OnInit {

  name : string = 'Appareil';
  status : string = 'Statut';
  constructor(private deviceService: DevicesService,
              private route: ActivatedRoute) { }

  ngOnInit() {
    const id = this.route.snapshot.params['id'];
    this.name = (this.deviceService.getDeviceById(+id)).name;
    this.status = (this.deviceService.getDeviceById(+id)).status;
  }

}
