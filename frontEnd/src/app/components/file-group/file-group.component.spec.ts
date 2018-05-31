import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FileGroupComponent } from './file-group.component';

describe('FileGroupComponent', () => {
  let component: FileGroupComponent;
  let fixture: ComponentFixture<FileGroupComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FileGroupComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FileGroupComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
