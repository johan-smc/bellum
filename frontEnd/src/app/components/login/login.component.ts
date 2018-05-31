import { Component, OnInit } from '@angular/core';

import { ValidateService } from '../../services/validate.service';
import { AuthService } from '../../services/auth.service';
import { Router } from '@angular/router';

import { NgFlashMessageService } from 'ng-flash-messages';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  private username : string;
  private password : string;

  constructor(
    private validateService : ValidateService ,
    private authService : AuthService,
    private router : Router,
    private ngFlashMessageService: NgFlashMessageService
  ){ }

  ngOnInit() {

  }
  onLoginSubmit()
  {
    const user = {
      username : this.username,
      password : this.password,
    }
    if( !this.validateService.validateLogin(user) )
    {
      this.ngFlashMessageService.showFlashMessage({ messages:["Fill in all fields"], timeout : 1000, type : 'danger'} );
      return false;
    }
    this.authService.loginUser(user).subscribe(data =>{
      data = JSON.parse(data['_body']);
      if(data['success']){
        this.authService.storeUserData(data['token'],data['date']);
        this.ngFlashMessageService.showFlashMessage({ messages:["Welcon to Bellum"], timeout : 1000, type : 'success'} );
        window.location.href = '/home';
      }
      else{
        var message = data['non_field_errors'];
        message = message[0];
        this.ngFlashMessageService.showFlashMessage({ messages:[message], timeout : 1000, type : 'danger'} );
        this.router.navigate(['']);
      }
    });
  }
}
