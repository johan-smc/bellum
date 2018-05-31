import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import {GroupService} from '../../services/group.service'
import {UserService} from '../../services/user.service'

@Component({
  selector: 'app-create-group',
  templateUrl: './create-group.component.html',
  styleUrls: ['./create-group.component.css']
})
export class CreateGroupComponent implements OnInit {
  private name : string;
  private description : string;


  constructor(
    private router : Router ,
    private groupService : GroupService,
    private userService : UserService
  ) { }

  ngOnInit() {
  }
  onRegisterSubmit()
  {
    const group = {
      name: this.name,
      description: this.description
    }
    this.groupService.create_group(group).subscribe(data =>{
      data = JSON.parse(data['_body']);
    });
    this.router.navigate(['/home']);
  }
}
