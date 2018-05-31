import { Injectable } from '@angular/core';
import {Http, Headers} from "@angular/http";
import {EndPointService} from './end-point.service';
@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(
    private http : Http,
    private endPoint : EndPointService
  ) { }

  registerUser( user )
  {
    let headers = new Headers();
    headers.append('Content-Type','application/json');
    let ep = this.endPoint.prepEndPoint('register_user/');
    return this.http.post(ep, user,{headers:headers})
  }
}
