import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MyFirstComponent } from './my-first/my-first.component';
import { DevicesComponent } from './devices/devices.component';

import 'hammerjs';
import { DevicesService } from './services/device.service';
import { AuthComponent } from './auth/auth.component';
import { DeviceViewComponent } from './device-view/device-view.component';
import { Routes, RouterModule } from '@angular/router';
import { AuthService } from './services/auth.service';
import { SingleDeviceComponent } from './single-device/single-device.component';
import { FourOhFourComponent } from './four-oh-four/four-oh-four.component';
import { AuthGuard } from './services/auth-guard.service';
import { EditDeviceComponent } from './edit-device/edit-device.component';
import { UserListComponent } from './user-list/user-list.component';
import { UserService } from './services/User.service';
import { NewUserComponent } from './new-user/new-user.component';

const appRoutes: Routes = [
  {path: "devices", canActivate: [AuthGuard], component: DeviceViewComponent},
  {path: "auth", component: AuthComponent},
  {path: "devices/:id", canActivate: [AuthGuard], component: SingleDeviceComponent},
  {path: "edit", canActivate: [AuthGuard], component: EditDeviceComponent},
  {path: "users", component: UserListComponent},
  {path: "new-user", component: NewUserComponent}, 
  {path: "", component: DeviceViewComponent},
  {path: "not-found", component: FourOhFourComponent},
  {path: "**", redirectTo: "/not-found"}
];

@NgModule({
  declarations: [
    AppComponent,
    MyFirstComponent,
    DevicesComponent,
    AuthComponent,
    DeviceViewComponent,
    SingleDeviceComponent,
    FourOhFourComponent,
    EditDeviceComponent,
    UserListComponent,
    NewUserComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    RouterModule.forRoot(appRoutes)
  ],
  providers: [
    DevicesService,
    AuthService,
    AuthGuard,
    UserService
  ],
  bootstrap: [AppComponent]
})


export class AppModule { }
