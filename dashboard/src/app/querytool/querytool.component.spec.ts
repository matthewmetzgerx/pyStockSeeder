import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { QuerytoolComponent } from './querytool.component';

describe('QuerytoolComponent', () => {
  let component: QuerytoolComponent;
  let fixture: ComponentFixture<QuerytoolComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ QuerytoolComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(QuerytoolComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
