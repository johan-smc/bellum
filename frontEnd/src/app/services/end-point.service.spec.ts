import { TestBed, inject } from '@angular/core/testing';

import { EndPointService } from './end-point.service';

describe('EndPointService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [EndPointService]
    });
  });

  it('should be created', inject([EndPointService], (service: EndPointService) => {
    expect(service).toBeTruthy();
  }));
});
