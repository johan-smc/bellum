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
import { CoreComponent } from './components/core/core.component';
import { CreateGroupComponent } from './components/create-group/create-group.component';
import { DeleteGroupComponent } from './components/delete-group/delete-group.component'
import { FileUploadModule } from 'ng2-file-upload';
import { ChangePasswordComponent } from './components/change-password/change-password.component';
import { FileGroupComponent } from './components/file-group/file-group.component';
import { UserGroupComponent } from './components/user-group/user-group.component';
import { AboutComponent } from './components/about/about.component';
import { DeleteFileComponent } from './components/delete-file/delete-file.component';


const appRoutes: Routes =[
    {path : '' , component : LoginComponent },
    {path : 'register' , component : RegisterComponent },
    {path : 'home' , component : HomeComponent },
    {path : 'create_group' , component : CreateGroupComponent },
    {path : 'delete_group' , component : DeleteGroupComponent },
    {path : 'delete_file' , component : DeleteFileComponent },
    {path : 'change_pass' , component : ChangePasswordComponent },
    {path : 'file_group' , component : FileGroupComponent },
    {path : 'user_group' , component : UserGroupComponent },
    {path : 'about' , component : AboutComponent },
    {path: '**', redirectTo: '/'},
];

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    HomeComponent,
    RegisterComponent,
    CoreComponent,
    CreateGroupComponent,
    DeleteGroupComponent,
    ChangePasswordComponent,
    FileGroupComponent,
    UserGroupComponent,
    AboutComponent,
    DeleteFileComponent,
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot(appRoutes),
    FormsModule,
    HttpModule,
    NgFlashMessagesModule.forRoot(),
    NgbModule.forRoot(),
    FileUploadModule,

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
