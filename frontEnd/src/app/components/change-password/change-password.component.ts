import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ChangePassService } from  '../../services/change-pass.service' ;
import { NgFlashMessageService } from 'ng-flash-messages';


@Component({
  selector: 'app-change-password',
  templateUrl: './change-password.component.html',
  styleUrls: ['./change-password.component.css']
})
export class ChangePasswordComponent implements OnInit {

  private password : string;
  private password_confirm : string;

  private samePassword : boolean;
  private strongerPassword : boolean;

  constructor(
    private changePassService : ChangePassService,
    private router : Router,
    private ngFlashMessageService: NgFlashMessageService
  ) {
      this.resetValid();
    }

  ngOnInit() {
  }

  onRegisterSubmit(){
    this.resetValid();
    const new_pass = {
      password : this.password
    }

    if( !this.isStrongerPassword() )
    {
      this.strongerPassword = false;
      return false;
    }

    if( this.password != this.password_confirm )
    {
      this.samePassword = false;
      return false;
    }

    this.changePassService.change_password(new_pass).subscribe(data=>{
      console.log(new_pass);
      data = JSON.parse(data['_body']);
      window.location.href = '/home';

    });
    // this.router.navigate(['/home']);
  }

  resetValid()
  {
    this.samePassword = true;
    this.strongerPassword = true;
  }
  isStrongerPassword()
  {
    var regexp = new RegExp('^(?=.*[A-Za-z])(?=.*\\d)(?=.*[$@$!%*#?&])[A-Za-z\\d$@$!%*#?&]{8,}$');
    return regexp.test(this.password);
  }

}
