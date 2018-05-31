import { Component, OnInit } from '@angular/core';
import {NgbModule} from '@ng-bootstrap/ng-bootstrap'
import {HomeService} from '../../services/home.service';

import './js/script.js'

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  private groups : any;
  constructor(
    private homeService : HomeService,
  ) { }

  ngOnInit() {
    this.homeService.get_UserGroups().subscribe(data =>{
      data = JSON.parse(data['_body']);
      this.groups = data ;
    });
  }

}
