import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {PortfolioComponent} from './portfolio/portfolio.component';
import {QuerytoolComponent} from './querytool/querytool.component';
import {HomeComponent} from './home/home.component';

const routes: Routes = [
  { path: 'portfolio', component: PortfolioComponent },
  { path: 'querytool', component: QuerytoolComponent },
  { path: '', component: HomeComponent }

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
