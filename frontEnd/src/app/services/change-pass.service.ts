import { Injectable } from '@angular/core';
import {Http, Headers} from "@angular/http";
import {EndPointService} from './end-point.service';
import {AuthService} from './auth.service';

@Injectable({
  providedIn: 'root'
})
export class ChangePassService {

  constructor(
    private http : Http,
    private endPoint : EndPointService,
    private authService : AuthService,

  ) { }

  change_password(pass){
    let headers = new Headers();
    headers.append('Content-Type','application/json');
    headers.append('Authorization','Token '+this.authService.getToken());
    let ep = this.endPoint.prepEndPoint('update_pass/');
    return this.http.post(ep, pass,{headers:headers})
  }

}
