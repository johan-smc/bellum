import { Injectable } from '@angular/core';
import {Http, Headers} from "@angular/http";
import {EndPointService} from './end-point.service';
import {AuthService} from './auth.service';

@Injectable({
  providedIn: 'root'
})
export class FileService {

  constructor(
    private http : Http,
    private endPoint : EndPointService,
    private authService : AuthService
  ) { }

  getFiles(father)
  {
    let headers = new Headers();
    headers.append('Content-Type','application/json');
    headers.append('Authorization','Token '+this.authService.getToken());
    let ep = this.endPoint.prepEndPoint('get_inodes/');
    return this.http.post(ep, father,{headers:headers})
  }

  getFile(file)
  {
    let headers = new Headers();
    headers.append('Content-Type','application/json');
    headers.append('Authorization','Token '+this.authService.getToken());
    let ep = this.endPoint.prepEndPoint('get_file/');
    return this.http.post(ep, file,{headers:headers})
  }
}
