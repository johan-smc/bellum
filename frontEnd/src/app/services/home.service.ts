import { Injectable } from '@angular/core';
import {Http, Headers} from "@angular/http";
import {tokenNotExpired} from 'angular2-jwt';
import {EndPointService} from './end-point.service';
import { AuthService } from './auth.service';

@Injectable({
  providedIn: 'root'
})
export class HomeService {

  private loggedInStatus = false;

  constructor(
    private http : Http,
    private endPoint : EndPointService,
    private authService : AuthService
  ) {
      this.loggedInStatus = !!localStorage.getItem('token');
   }

   get_UserGroups(){
     var token = this.authService.getToken()
     let headers = new Headers();
     headers.append('Content-Type','application/json');
     headers.append('Authorization','Token '+token);
     let ep = this.endPoint.prepEndPoint('get_groups/');
     return this.http.get(ep,{headers:headers})
   }

   get_UserOwner(){
     var token = this.authService.getToken()
     let headers = new Headers();
     headers.append('Content-Type','application/json');
     headers.append('Authorization','Token '+token);
     let ep = this.endPoint.prepEndPoint('get_groups_owner/');
     return this.http.get(ep,{headers:headers})
   }

   

}
