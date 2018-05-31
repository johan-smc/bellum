import { Component, OnInit } from '@angular/core';


import { ValidateService } from '../../services/validate.service';
import { UserService } from '../../services/user.service';
import { Router } from '@angular/router';

import { NgFlashMessageService } from 'ng-flash-messages';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  private username : string;
  private password : string;
  private password_confirm : string;
  private name : string;
  private email : string;

  private validEmail : boolean;
  private emailToken : boolean;
  private userNameToken : boolean;
  private samePassword : boolean;
  private strongerPassword : boolean;

  constructor(
      private validateService : ValidateService ,
      private userService : UserService,
      private router : Router,
      private ngFlashMessageService: NgFlashMessageService
  ) {
    this.resetValid()
   }

  ngOnInit() {
  }

  onRegisterSubmit()
  {
    this.resetValid();
    const user = {
      username : this.username,
      password : this.password,
      my_user:{
        name: this.name,
        email: this.email
      }
    }
    if( !this.isStrongerPassword() )
    {
      this.strongerPassword = false;
      return false;
    }
    if( !this.validateService.validateEmail(this.email) )
    {
      this.validEmail = false;
      return false;
    }
    if( this.password != this.password_confirm )
    {
      this.samePassword = false;
      return false;
    }
    this.userService.registerUser(user).subscribe(data =>{
      data = JSON.parse(data['_body']);
      if(data['success']){
        this.ngFlashMessageService.showFlashMessage({ messages:["Register complete"], timeout : 1000, type : 'success'} );
        this.router.navigate(['']);
      }
      else{
        if( data['username'] )
          this.userNameToken = false;
        if( data['my_user']  )
          this.emailToken = false;
      }
    });
  }
  resetValid()
  {
    this.validEmail = true;
    this.emailToken = true;
    this.userNameToken = true;
    this.samePassword = true;
    this.strongerPassword = true;
  }
  isStrongerPassword()
  {
    var regexp = new RegExp('^(?=.*[A-Za-z])(?=.*\\d)(?=.*[$@$!%*#?&])[A-Za-z\\d$@$!%*#?&]{8,}$');
    return regexp.test(this.password);
  }

}
