import { Injectable } from '@angular/core';
import {Http, Headers} from "@angular/http";
import {EndPointService} from './end-point.service';
import {AuthService} from './auth.service';


@Injectable({
  providedIn: 'root'
})
export class TimeDiffService {

  constructor(
    private http : Http,
    private endPoint : EndPointService,
    private authService : AuthService,
  ) { }

  get_last_pass(){
    let headers = new Headers();
    headers.append('Content-Type','application/json');
    headers.append('Authorization','Token '+this.authService.getToken());
    let ep = this.endPoint.prepEndPoint('last_time/');
    return this.http.get(ep, pass,{headers:headers})
  }

  get_actual_time(){
    let headers = new Headers();
    headers.append('Content-Type','application/json');
    headers.append('Authorization','Token '+this.authService.getToken());
    let ep = this.endPoint.prepEndPoint('time_now/');
    return this.http.get(ep, pass,{headers:headers})
  }

}
