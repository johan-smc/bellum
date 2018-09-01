import { Component, OnInit } from '@angular/core';
import {UserService} from '../../services/user.service';
import { Router } from '@angular/router';
import {HomeService} from '../../services/home.service';
import { NgFlashMessageService } from 'ng-flash-messages'

@Component({
  selector: 'app-user-group',
  templateUrl: './user-group.component.html',
  styleUrls: ['./user-group.component.css']
})
export class UserGroupComponent implements OnInit {
  private users : any;
  private groups : any;
  private user_sel : any;
  private group_sel : any;


  constructor(
    private userService : UserService,
    private router : Router ,
    private homeService : HomeService,
    private ngFlashMessageService: NgFlashMessageService

  ) {
    this.homeService.get_UserGroups().subscribe(data =>{
      data = JSON.parse(data['_body']);
      this.groups = data ;
    });
    this.userService.get_all_users().subscribe(data=>{
      data = JSON.parse(data['_body']);
      this.users = data;
    });
  }

  ngOnInit() {
  }

  submitUnion(){
    const info ={
      idGroup : this.group_sel.id,
      idUsr : this.user_sel.id,
    }
    this.userService.unionUserGroup(info).subscribe(data =>{
      this.ngFlashMessageService.showFlashMessage({ messages:["Ok union"], timeout : 1000, type : 'success'} );
      data = JSON.parse(data['_body']);
    });

  }

}
