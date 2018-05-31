import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { RouterModule , Routes } from '@angular/router'
import { FormsModule }   from '@angular/forms';

import { HttpModule } from '@angular/http';

import { NgFlashMessagesModule } from 'ng-flash-messages';

import { AppComponent } from './app.component';
import { LoginComponent } from './components/login/login.component';

import { ValidateService } from './services/validate.service';
import { AuthService } from './services/auth.service';
import { EndPointService } from './services/end-point.service';
import { UserService } from './services/user.service';
import { FileService } from './services/file.service';
import { HomeComponent } from './components/home/home.component';
import { RegisterComponent } from './components/register/register.component';

import {NgbModule} from '@ng-bootstrap/ng-bootstrap';
import { CoreComponent } from './components/core/core.component'

const appRoutes: Routes =[
    {path : '' , component : LoginComponent },
    {path : 'register' , component : RegisterComponent },
    {path : 'home' , component : HomeComponent },
    {path: '**', redirectTo: '/404'},
];

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    HomeComponent,
    RegisterComponent,
    CoreComponent,
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot(appRoutes),
    FormsModule,
    HttpModule,
    NgFlashMessagesModule.forRoot(),
    NgbModule.forRoot(),

  ],
  providers: [
    ValidateService,
    AuthService,
    EndPointService,
    UserService,
    FileService,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
