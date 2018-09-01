import { Injectable } from '@angular/core';
import {Http, Headers} from "@angular/http";
import {tokenNotExpired} from 'angular2-jwt';
import {EndPointService} from './end-point.service';
import { AuthService } from './auth.service';

@Injectable({
  providedIn: 'root'
})
export class DeleteFilesService {
  public token : any;
  private user : any;
  private loggedInStatus = false;
  constructor(
    private http : Http,
    private endPoint : EndPointService,
    private authService : AuthService
  ){
    this.loggedInStatus = !!localStorage.getItem('token');
  }
  delFile(file_id){
    console.log("---> " + file_id);
    var token = this.authService.getToken();
    let headers = new Headers();
    headers.append('Content-Type','application/json');
    headers.append('Authorization','Token '+token);
    let ep = this.endPoint.prepEndPoint('del_group/');
    return this.http.post(ep, file_id,{headers:headers})
  }


}
