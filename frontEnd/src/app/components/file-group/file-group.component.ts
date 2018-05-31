import { Component, OnInit } from '@angular/core';
import {HomeService} from '../../services/home.service';
import { Router } from '@angular/router';
import {FileService} from '../../services/file.service'
import { NgFlashMessageService } from 'ng-flash-messages';


@Component({
  selector: 'app-file-group',
  templateUrl: './file-group.component.html',
  styleUrls: ['./file-group.component.css']
})
export class FileGroupComponent implements OnInit {


  private files : any;
  private groups : any;
  private file_sel : any;
  private group_sel : any;

  constructor(
    private homeService : HomeService,
    private router : Router ,
    private fileService : FileService,
    private ngFlashMessageService: NgFlashMessageService

  ) {
    this.homeService.get_UserGroups().subscribe(data =>{
      data = JSON.parse(data['_body']);
      this.groups = data ;
    });
    this.fileService.getAllFiles().subscribe(data=>{
      data = JSON.parse(data['_body']);
      this.files = data;
    });
  }

  ngOnInit() {

  }

  submitUnion(){
    const info ={
      group : this.group_sel.id,
      inode : this.file_sel.id,
      permission : 3,
    }
    this.fileService.unionFileGroup(info).subscribe(data =>{
      this.ngFlashMessageService.showFlashMessage({ messages:["Ok union"], timeout : 1000, type : 'success'} );
      data = JSON.parse(data['_body']);
    });
  }
}
