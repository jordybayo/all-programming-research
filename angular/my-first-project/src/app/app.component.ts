import { Component, OnInit, OnDestroy } from '@angular/core';
import { DevicesService } from './services/device.service';
import { interval, Subscription } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})


export class AppComponent implements OnInit, OnDestroy{

    secondes: number;
    counterSubscription: Subscription;

    constructor(){

    }

    ngOnInit(): void {
      const counter = interval(1000);
      this.counterSubscription = counter.subscribe(
        (value: number)=>{
          this.secondes = value;
        },
        (error: any)=>{
          console.log("une erreur a ete rencontre !");
        },
        (/*complete*/)=>{
          console.log("Observalbes completes");
        }
      );
    }

    ngOnDestroy(): void {
      this.counterSubscription.unsubscribe();
    }
}
