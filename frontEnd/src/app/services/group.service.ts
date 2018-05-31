import { Injectable } from '@angular/core';
import { AuthService } from './auth.service';
import {Http, Headers} from "@angular/http";
import {tokenNotExpired} from 'angular2-jwt';
import {EndPointService} from './end-point.service';

@Injectable({
  providedIn: 'root'
})

export class GroupService {
  private loggedInStatus = false;
  constructor(
      private http : Http,
      private endPoint : EndPointService,
      private authService : AuthService
    ) {
      this.loggedInStatus = !!localStorage.getItem('token');
    }

    create_group(group)
    {
      var token = this.authService.getToken()
      let headers = new Headers();
      headers.append('Content-Type','application/json');
      headers.append('Authorization','Token '+token);
      let ep = this.endPoint.prepEndPoint('register_group/');
      return this.http.post(ep, group,{headers:headers})
    }


}
