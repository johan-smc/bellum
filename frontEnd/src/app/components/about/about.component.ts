import { Component, OnInit } from '@angular/core';
import {UserService} from '../../services/user.service';

@Component({
  selector: 'app-about',
  templateUrl: './about.component.html',
  styleUrls: ['./about.component.css']
})
export class AboutComponent implements OnInit {
  private users : any;

  constructor(
    private userService : UserService,
  ) {
    this.userService.get_all_users().subscribe(data=>{
      data = JSON.parse(data['_body']);
      console.log(data);
      this.users = data;
    });
  }

  ngOnInit() {
  }

}
