import { Component, OnInit,Input } from '@angular/core';

import { FileService } from '../../services/file.service';
import { AuthService } from '../../services/auth.service';
import { GroupService } from '../../services/group.service';
import { UserService } from '../../services/user.service';
import { NgFlashMessageService } from 'ng-flash-messages';


@Component({
  selector: 'app-core',
  templateUrl: './core.component.html',
  styleUrls: ['./core.component.css']
})
export class CoreComponent implements OnInit {
  public idGroup: string = "";
  private files : any;
  private namefile : string;
  private namefolder : string;
  private idFather : number;

  fileToUpload: File = null;
  constructor(
    private fileService : FileService,
    private ngFlashMessageService: NgFlashMessageService,
    private authService: AuthService,
    private groupService: GroupService,
    private userService: UserService,
  ) {
    this.refresh(null);
   }

  ngOnInit() {
  }

  getFiles(father_id)
  {
    this.idFather = father_id;
    const father = {
      father : father_id,
    }
    this.fileService.getFiles(father).subscribe(data=>{
      data = JSON.parse(data['_body']);
      this.files = data;
      this.userService.get_usr_id().subscribe(info=>{
        info = JSON.parse(info['_body']);
        for( var i =0 ; i < this.files.length ; ++i )
        {
          this.files[i]['change']=this.files[i]['last_user_mod']['id']!=info['id'];
        }

      });
    });
  }
  getFilesGroup(father_id)
  {
    this.idFather = father_id;
    const father = {
      group_id: this.idGroup,
      father : father_id,
    }
    this.fileService.getFilesGroup(father).subscribe(data=>{
      data = JSON.parse(data['_body']);
      this.files = data;
      this.userService.get_usr_id().subscribe(info=>{
        info = JSON.parse(info['_body']);
        for( var i =0 ; i < this.files.length ; ++i )
        {
          this.files[i]['change']=this.files[i]['last_user_mod']['id']!=info['id'];
        }

      });
    });
  }
  dowloadOnClick(id)
  {
    const file = {
      id_file : id
    }
    this.fileService.getFile(file).subscribe(data=>{
      console.log(data);
      var type = data['headers']['_headers'].get('content-type')[0]
      data = data['_body'];

      var blob = new Blob([data], { type: 'plain/text' });
        // console.log(blob);
        var url= window.URL.createObjectURL(blob);
        // console.log(url);
        window.location.href = url;
    });
  }
  handleFileInput(files: FileList) {
    this.fileToUpload = files.item(0);
  }
  uploadFileToActivity() {
    this.fileService.postFile(this.fileToUpload,this.namefile,this.idFather).subscribe(data => {
      console.log(data);
      this.ngFlashMessageService.showFlashMessage({ messages:["Save file correct"], timeout : 1000, type : 'success'} );
      this.refresh(this.idFather);
      }, error => {
        console.log(error);
      });
  }
  createFolder()
  {
    const folder={
      name : this.namefolder,
      father : this.idFather
    };
    this.fileService.createFolder(folder).subscribe(data => {

      this.ngFlashMessageService.showFlashMessage({ messages:["Save folder correct"], timeout : 1000, type : 'success'} );
      this.refresh(this.idFather);
      }, error => {
        console.log(error);
      });
  }
  changeDate()
  {
    // var dateNow = new Date();
    // var dateU = new Date(this.authService.getDate());
    // var limit : number = 2629746000;
    // var diff: number = dateNow-dateU;
    // if(  diff > limit )
    //   return true;
    return false;
  }

  refresh(father)
  {
    if( this.idGroup == "" )
      this.getFiles(father);
    else
      this.getFilesGroup(father);
  }

  ngDoCheck()
  {
    if( this.idGroup != this.groupService.getGroup() )
    {
      this.idGroup = this.groupService.getGroup();
      this.refresh(this.idFather);
    }

  }
  replaceFile(id_file)
  {
    console.log(id_file);
    this.fileService.uploadFile(this.fileToUpload,id_file).subscribe(data => {
      console.log(data);
      this.ngFlashMessageService.showFlashMessage({ messages:["Save file correct"], timeout : 1000, type : 'success'} );
      this.refresh(this.idFather);
      }, error => {
        console.log(error);
      });
  }


}
