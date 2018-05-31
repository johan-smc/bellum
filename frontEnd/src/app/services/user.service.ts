import { Injectable } from '@angular/core';
import {Http, Headers} from "@angular/http";
import {EndPointService} from './end-point.service';
import {AuthService} from './auth.service';
@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(
    private http : Http,
    private endPoint : EndPointService,
    private authService : AuthService,

  ) { }

  registerUser( user )
  {
    let headers = new Headers();
    headers.append('Content-Type','application/json');
    let ep = this.endPoint.prepEndPoint('register_user/');
    return this.http.post(ep, user,{headers:headers})
  }
  get_usrid()
  {
    var token = this.authService.getToken()
    let headers = new Headers();
    headers.append('Content-Type','application/json');
    headers.append('Authorization','Token '+token);
    let ep = this.endPoint.prepEndPoint('get_groups_owner/');
    return this.http.get(ep,{headers:headers})
  }
}
