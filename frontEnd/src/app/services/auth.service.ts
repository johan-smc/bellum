import { Injectable } from '@angular/core';
import {Http, Headers} from "@angular/http";
import {tokenNotExpired} from 'angular2-jwt';
import {EndPointService} from './end-point.service';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  public token : any;
  private user : any;
  private date : any;
  private loggedInStatus = false;

  constructor(
    private http : Http,
    private endPoint : EndPointService
  )
  {
    this.loggedInStatus = !!localStorage.getItem('token');
  }
  loginUser( user ){
    let headers = new Headers();
    headers.append('Content-Type','application/json');
    let ep = this.endPoint.prepEndPoint('token/');
    return this.http.post(ep, user,{headers:headers})

  }
  storeUserData(token,date){
    localStorage.setItem('token',token);
    localStorage.setItem('date',JSON.stringify(date));
    this.token = token;
    this.date = date;
  }
  getToken()
  {
    return localStorage.getItem('token');
  }
  getUser()
  {
    return JSON.parse(localStorage.getItem('user'));
  }
  getDate()
  {
    return localStorage.getItem('date');
  }

}
