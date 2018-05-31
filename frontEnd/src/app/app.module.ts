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

const appRoutes: Routes =[
    {path : '' , component : LoginComponent },
    {path: '**', redirectTo: '/404'},
];

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot(appRoutes),
    FormsModule,
    HttpModule,
    NgFlashMessagesModule.forRoot(),
  ],
  providers: [
    ValidateService,
    AuthService,
    EndPointService,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
