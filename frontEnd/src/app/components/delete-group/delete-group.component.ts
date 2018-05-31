import { Component, OnInit } from '@angular/core';
import {NgbModule} from '@ng-bootstrap/ng-bootstrap'
import {HomeService} from '../../services/home.service';
import { Router } from '@angular/router';
import {DeleteFilesService} from '../../services/delete-files.service'


@Component({
  selector: 'app-delete-group',
  templateUrl: './delete-group.component.html',
  styleUrls: ['./delete-group.component.css']
})
export class DeleteGroupComponent implements OnInit {
  private groups : any;
  private group_sel: any ;
  constructor(
      private homeService : HomeService,
      private router : Router ,
      private deleteFilesService : DeleteFilesService

  ) { }

  ngOnInit() {
    this.homeService.get_UserOwner().subscribe(data =>{
      data = JSON.parse(data['_body']);
      this.groups = data ;
    });
  }
  onRegisterSubmit(){
    const info = {
      id : this.group_sel.id
    }
    this.deleteFilesService.delFile(info).subscribe(data =>{
      data = JSON.parse(data['_body']);
      this.router.navigate(['/home']);
    });

  }

}
