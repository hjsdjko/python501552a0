<template>
<div class="home-preview" :style='{"margin":"0px auto","flexWrap":"wrap","flexDirection":"row","background":"#fff","display":"flex","width":"100%","justifyContent":"center"}'>



		<!-- 关于我们 -->
		<div id="about" class="animate__animated" :style='{"minHeight":"600px","padding":"0 12%","boxShadow":"0 0px 0px rgba(255, 255, 255, .3)","margin":"80px 0 0","alignItems":"flex-start","flexWrap":"wrap","background":"#fff","display":"flex","width":"100%","position":"relative","height":"auto","order":"1"}'>
		  <div :style='{"padding":"0px","margin":"0 auto","color":"#000","top":"80px","textAlign":"left","background":"none","width":"auto","fontSize":"22px","lineHeight":"22px","position":"absolute","fontWeight":"500","order":"2"}'>{{aboutUsDetail.title}}</div>
		  <div :style='{"margin":"0px 0 20px","color":"#000","top":"0","textAlign":"left","display":"block","width":"auto","lineHeight":"60px","fontSize":"42px","position":"absolute","fontWeight":"600"}'>{{aboutUsDetail.subtitle}}</div>
		  <div :style='{"padding":"0px","margin":"0","flexWrap":"wrap","display":"flex","width":"auto","height":"auto","order":"5"}'>
		    <img :style='{"margin":"0 0px","objectFit":"cover","borderRadius":"0px","top":"0","display":"block","width":"26%","position":"absolute","right":"12%","height":"600px"}' :src="baseUrl + aboutUsDetail.picture1">
		    <img :style='{"margin":"0","objectFit":"cover","left":"12%","bottom":"0","display":"block","width":"22%","position":"absolute","height":"200px"}' :src="baseUrl + aboutUsDetail.picture2">
		    <img :style='{"margin":"0","objectFit":"cover","left":"36%","bottom":"0","display":"block","width":"23%","position":"absolute","height":"200px"}' :src="baseUrl + aboutUsDetail.picture3">
		  </div>
		  <div :style='{"padding":"0","margin":"150px 0 60px 0","overflow":"hidden","color":"#333","background":"#fff","width":"58%","fontSize":"16px","lineHeight":"30px","fontWeight":"600","height":"210px","order":"3"}' v-html="aboutUsDetail.content"></div>
		  <div :style='{"width":"315px","position":"absolute","top":"180px","background":"url(http://codegen.caihongy.cn/20231006/3fb7e07853594c3c9097d2bbe08a28bd.png) no-repeat","display":"none","height":"30px"}' />
		  <div :style='{"width":"285px","background":"url(http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg) 0% 0% / cover no-repeat","display":"none","height":"100px"}' />
		  <div :style='{"width":"285px","background":"url(http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg) 0% 0% / cover no-repeat","display":"none","height":"100px"}' />
		  <div :style='{"width":"285px","background":"url(http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg) 0% 0% / cover no-repeat","display":"none","height":"100px"}' />
		  <div :style='{"border":"0px solid #1d8001","cursor":"pointer","padding":"0 20px 0 0","margin":"0","textAlign":"right","display":"block","right":"43%","top":"20px","background":"url(http://codegen.caihongy.cn/20231010/b345185c76ac4a77bf4cd6f6171a72ed.png) no-repeat center top / 100% 100%","width":"240px","lineHeight":"73px","position":"absolute","height":"80px"}' @click="toDetail('aboutusDetail',aboutUsDetail)">
		    <span :style='{"color":"#333","letterSpacing":"0px","fontSize":"14px"}'>查看更多</span>
		    <span class="icon iconfont icon-jiantou09" :style='{"color":"#333","fontSize":"16px","display":"none"}'></span>
		  </div>
		</div>
		<!-- 关于我们 -->

		<!-- 系统简介 -->
		<div id="system" class="animate__animated" :style='{"padding":"0 12% 80px","margin":"0 auto","flexWrap":"wrap","background":"#f1f1f1","display":"flex","width":"100%","position":"relative","justifyContent":"space-between","height":"auto","order":"4"}'>
		  <div :style='{"padding":"0px 0 0","margin":"10px auto 0","color":"#000","textAlign":"left","background":"none","width":"100%","fontSize":"22px","fontWeight":"500","height":"60px","order":"2"}'>{{systemIntroductionDetail.title}}</div>
		  <div :style='{"margin":"50px auto 0","color":"#000","textAlign":"left","display":"block","width":"100%","lineHeight":"1.5","fontSize":"42px","fontWeight":"600"}'>{{systemIntroductionDetail.subtitle}}</div>
		  <div :style='{"width":"49%","padding":"0","background":"#f00","height":"600px","order":"3"}'>
		    <img :style='{"width":"100%","margin":"0","objectFit":"cover","display":"block","height":"100%"}' :src="baseUrl + systemIntroductionDetail.picture1">
		    <img :style='{"width":"43%","margin":"0","objectFit":"contain","display":"none","height":"80%"}' :src="baseUrl + systemIntroductionDetail.picture2">
		    <img :style='{"margin":"0 10px","objectFit":"cover","flex":1,"display":"none","height":"120px"}' :src="baseUrl + systemIntroductionDetail.picture3">
		  </div>
		  <div :style='{"padding":"0px","margin":"160px 0 40px 0","overflow":"hidden","color":"#333","background":"none","width":"49%","lineHeight":"30px","fontSize":"16px","fontWeight":"500","height":"150px","order":"4"}' v-html="systemIntroductionDetail.content"></div>
		  <div :style='{"width":"100%","margin":"40px 0 0","background":"url(http://codegen.caihongy.cn/20231010/fa45131753e2441b8eb1996ef7443eb8.png) no-repeat center top / 100% 100%","display":"block","height":"139px","order":"9"}' />
		  <div :style='{"width":"285px","background":"url(http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg) 0% 0% / cover no-repeat","display":"none","height":"100px"}' />
		  <div :style='{"width":"285px","background":"url(http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg) 0% 0% / cover no-repeat","display":"none","height":"100px"}' />
		  <div :style='{"width":"285px","background":"url(http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg) 0% 0% / cover no-repeat","display":"none","height":"100px"}' />
		  <div :style='{"border":"0px solid #1d8001","cursor":"pointer","padding":"0 10px 0 0","margin":"0","textAlign":"right","bottom":"450px","display":"block","justifyContent":"center","left":"calc(51% + 0px)","background":"url(http://codegen.caihongy.cn/20231010/b72adcd3865b46389aba91ec7423d34c.png) no-repeat center top / 100% 100%","width":"240px","lineHeight":"59px","position":"absolute","order":"8","height":"59px"}' @click="toDetail('systemintroDetail',systemIntroductionDetail)">
		    <span :style='{"padding":"0 6px 0 0","margin":"0","color":"#fff","background":"none","display":"inline-block","width":"auto","fontSize":"16px","lineHeight":"60px","height":"auto"}'>查看更多</span>
		    <span class="icon iconfont icon-jiantou09" :style='{"padding":"0px","margin":"0","color":"#1d8001","background":"none","display":"none","fontSize":"16px","lineHeight":"40px","height":"40px"}'></span>
		  </div>
		</div>
		<!-- 系统简介 -->
		
	<!-- 新闻资讯 -->
	<div id="animate_newsnews" class="news animate__animated" :style='{"padding":"0","margin":"40px auto 40px","background":"url(),#fff","flex":"1","width":"100%","position":"relative","order":"5"}'>
		<div v-if="false" class="idea newsIdea" :style='{"padding":"20px","flexWrap":"wrap","background":"#efefef","justifyContent":"space-between","display":"flex"}'>
			<div class="box1" :style='{"width":"20%","background":"#fff","height":"80px"}'></div>
			<div class="box2" :style='{"width":"20%","background":"#fff","height":"80px"}'></div>
			<div class="box3" :style='{"width":"20%","background":"#fff","height":"80px"}'></div>
			<div class="box4" :style='{"width":"20%","background":"#fff","height":"80px"}'></div>
			<div class="box5" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
			<div class="box6" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
			<div class="box7" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
			<div class="box8" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
			<div class="box9" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
			<div class="box10" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		</div>
		
		<div class="title" :style='{"width":"76%","padding":"36px 0 0","margin":"0px auto","textAlign":"left","background":"url() no-repeat left top / auto 42px","height":"100px"}'>
			<span :style='{"color":"#000","fontSize":"32px","fontWeight":"600"}'>通知公告</span>
		</div>
		
			
			
			
			
			
			<!-- 样式五 -->
		<div v-if="newsList.length" class="list list5 index-pv1" :style='{"width":"100%","padding":"20px 12%","fontSize":"14px","color":"#999","background":"#fff","height":"auto"}'>
		  <div @click="toDetail('newsDetail', newsList[0])" v-if="newsList.length>0" class="list-item animation-box" :style='{"cursor":"pointer","width":"100%","margin":"0 0 30px","background":"none","height":"520px"}'>
		    <img :style='{"width":"40%","objectFit":"cover","float":"left","height":"100%"}' :src="baseUrl + newsList[0].picture" alt="">
		    <div :style='{"padding":"40px","boxShadow":"1px 2px 9px #ccc","textAlign":"right","background":"#fff","display":"inline-block","width":"60%","position":"relative","float":"right","height":"100%"}'>
		      <div :style='{"padding":"10px","margin":"0 0 60px","overflow":"hidden","color":"#333","textAlign":"left","background":"none","lineHeight":"40px","fontSize":"18px","height":"80px"}' class="new5-one-info-title line1">{{newsList[0].title}}</div>
		      <div :style='{"padding":"10px","margin":"0 0 120px","overflow":"hidden","color":"#999","textAlign":"left","background":"none","lineHeight":"40px","fontSize":"16px","height":"140px"}' class="new5-one-info-descript line3">{{newsList[0].introduction}}</div>
			  <div :style='{"float":"left","padding":"0 10px","display":"inline-block"}'>
			    <span class="icon iconfont icon-shijian21" :style='{"margin":"0 2px 0 0","lineHeight":"1.5","fontSize":"inherit","color":"inherit","display":"none"}'></span>
			    <span class="text" :style='{"color":"inherit","lineHeight":"1.5","fontSize":"inherit"}'>{{newsList[0].addtime}}</span>
			  </div>
			  <div :style='{"padding":"0 10px","position":"absolute","top":"400px","float":"left","left":"40px","display":"inline-block"}'>
			    <span class="icon iconfont icon-geren16" :style='{"margin":"0 2px 0 0","lineHeight":"1.5","fontSize":"inherit","color":"inherit"}'></span>
			    <span class="text" :style='{"color":"inherit","lineHeight":"1.5","fontSize":"inherit"}'>{{newsList[0].name}}</span>
			  </div>
			  <div :style='{"padding":"0 10px","display":"inline-block"}'>
			    <span class="icon iconfont icon-zan10" :style='{"margin":"0 2px 0 0","lineHeight":"1.5","fontSize":"inherit","color":"inherit"}'></span>
			    <span class="text" :style='{"color":"inherit","lineHeight":"1.5","fontSize":"inherit"}'>{{newsList[0].thumbsupnum}}</span>
			  </div>
			  <div :style='{"padding":"0 10px","display":"inline-block"}'>
			    <span class="icon iconfont icon-shoucang10" :style='{"margin":"0 2px 0 0","lineHeight":"1.5","fontSize":"inherit","color":"inherit"}'></span>
			    <span class="text" :style='{"color":"inherit","lineHeight":"1.5","fontSize":"inherit"}'>{{newsList[0].storeupnum}}</span>
			  </div>
			  <div :style='{"padding":"0 10px","display":"inline-block"}'>
			    <span class="icon iconfont icon-chakan2" :style='{"margin":"0 2px 0 0","lineHeight":"1.5","fontSize":"inherit","color":"inherit"}'></span>
			    <span class="text" :style='{"color":"inherit","lineHeight":"1.5","fontSize":"inherit"}'>{{newsList[0].clicknum}}</span>
			  </div>
			</div>
		  </div>
		  <div :style='{"width":"100%","flexWrap":"wrap","background":"#fff","justifyContent":"space-between","display":"flex","height":"275px"}' class="list-body">
		    <div @click="toDetail('newsDetail', newsList[1])" v-if="newsList.length>1" class="new5-item animation-box" :style='{"cursor":"pointer","padding":"20px","boxShadow":"1px 2px 9px #ccc","background":"#fff","width":"32%","position":"relative","height":"275px"}'>
		      <div :style='{"padding":"0 10px","margin":"0 0 20px","overflow":"hidden","color":"#333","lineHeight":"40px","fontSize":"18px","height":"80px"}' class="new5-item-title line1">{{newsList[1].title}}</div>
		      <div :style='{"padding":"0 10px","margin":"0 0 20px","overflow":"hidden","color":"#999","lineHeight":"40px","fontSize":"16px","height":"80px"}' class="new5-item-descript line3">{{newsList[1].introduction}}</div>
			  <div :style='{"float":"right","padding":"0 10px","display":"inline-block"}'>
			    <span class="icon iconfont icon-shijian21" :style='{"margin":"0 2px 0 0","lineHeight":"1.5","fontSize":"inherit","color":"inherit","display":"none"}'></span>
			    <span class="text" :style='{"color":"inherit","lineHeight":"1.5","fontSize":"inherit"}'>{{newsList[1].addtime}}</span>
			  </div>
			  <div :style='{"padding":"0 10px","display":"inline-block"}'>
			    <span class="icon iconfont icon-geren16" :style='{"margin":"0 2px 0 0","lineHeight":"1.5","fontSize":"inherit","color":"inherit"}'></span>
			    <span class="text" :style='{"color":"inherit","lineHeight":"1.5","fontSize":"inherit"}'>{{newsList[1].name}}</span>
			  </div>
			  <div :style='{"padding":"0 10px","display":"inline-block"}'>
			    <span class="icon iconfont icon-zan10" :style='{"margin":"0 2px 0 0","lineHeight":"1.5","fontSize":"inherit","color":"inherit"}'></span>
			    <span class="text" :style='{"color":"inherit","lineHeight":"1.5","fontSize":"inherit"}'>{{newsList[1].thumbsupnum}}</span>
			  </div>
			  <div :style='{"padding":"0 10px","display":"inline-block"}'>
			    <span class="icon iconfont icon-shoucang10" :style='{"margin":"0 2px 0 0","lineHeight":"1.5","fontSize":"inherit","color":"inherit"}'></span>
			    <span class="text" :style='{"color":"inherit","lineHeight":"1.5","fontSize":"inherit"}'>{{newsList[1].storeupnum}}</span>
			  </div>
			  <div :style='{"padding":"0 10px","display":"inline-block"}'>
			    <span class="icon iconfont icon-chakan2" :style='{"margin":"0 2px 0 0","lineHeight":"1.5","fontSize":"inherit","color":"inherit"}'></span>
			    <span class="text" :style='{"color":"inherit","lineHeight":"1.5","fontSize":"inherit"}'>{{newsList[1].clicknum}}</span>
			  </div>
		    </div>
			<div @click="toDetail('newsDetail', newsList[2])" v-if="newsList.length>2" class="new5-item animation-box" :style='{"cursor":"pointer","padding":"20px","boxShadow":"1px 2px 9px #ccc","background":"#fff","width":"32%","position":"relative","height":"275px"}'>
			  <div :style='{"padding":"0 10px","margin":"0 0 20px","overflow":"hidden","color":"#333","lineHeight":"40px","fontSize":"18px","height":"80px"}' class="new5-item-title line1">{{newsList[2].title}}</div>
			  <div :style='{"padding":"0 10px","margin":"0 0 20px","overflow":"hidden","color":"#999","lineHeight":"40px","fontSize":"16px","height":"80px"}' class="new5-item-descript line3">{{newsList[2].introduction}}</div>
			  <div :style='{"float":"right","padding":"0 10px","display":"inline-block"}'>
			    <span class="icon iconfont icon-shijian21" :style='{"margin":"0 2px 0 0","lineHeight":"1.5","fontSize":"inherit","color":"inherit","display":"none"}'></span>
			    <span class="text" :style='{"color":"inherit","lineHeight":"1.5","fontSize":"inherit"}'>{{newsList[2].addtime}}</span>
			  </div>
			  <div :style='{"padding":"0 10px","display":"inline-block"}'>
			    <span class="icon iconfont icon-geren16" :style='{"margin":"0 2px 0 0","lineHeight":"1.5","fontSize":"inherit","color":"inherit"}'></span>
			    <span class="text" :style='{"color":"inherit","lineHeight":"1.5","fontSize":"inherit"}'>{{newsList[2].name}}</span>
			  </div>
			  <div :style='{"padding":"0 10px","display":"inline-block"}'>
			    <span class="icon iconfont icon-zan10" :style='{"margin":"0 2px 0 0","lineHeight":"1.5","fontSize":"inherit","color":"inherit"}'></span>
			    <span class="text" :style='{"color":"inherit","lineHeight":"1.5","fontSize":"inherit"}'>{{newsList[2].thumbsupnum}}</span>
			  </div>
			  <div :style='{"padding":"0 10px","display":"inline-block"}'>
			    <span class="icon iconfont icon-shoucang10" :style='{"margin":"0 2px 0 0","lineHeight":"1.5","fontSize":"inherit","color":"inherit"}'></span>
			    <span class="text" :style='{"color":"inherit","lineHeight":"1.5","fontSize":"inherit"}'>{{newsList[2].storeupnum}}</span>
			  </div>
			  <div :style='{"padding":"0 10px","display":"inline-block"}'>
			    <span class="icon iconfont icon-chakan2" :style='{"margin":"0 2px 0 0","lineHeight":"1.5","fontSize":"inherit","color":"inherit"}'></span>
			    <span class="text" :style='{"color":"inherit","lineHeight":"1.5","fontSize":"inherit"}'>{{newsList[2].clicknum}}</span>
			  </div>
			</div>
			<div @click="toDetail('newsDetail', newsList[3])" v-if="newsList.length>3" class="new5-item animation-box" :style='{"cursor":"pointer","padding":"20px","boxShadow":"1px 2px 9px #ccc","background":"#fff","width":"32%","position":"relative","height":"275px"}'>
			  <div :style='{"padding":"0 10px","margin":"0 0 20px","overflow":"hidden","color":"#333","lineHeight":"40px","fontSize":"18px","height":"80px"}' class="new5-item-title line1">{{newsList[3].title}}</div>
			  <div :style='{"padding":"0 10px","margin":"0 0 20px","overflow":"hidden","color":"#999","lineHeight":"40px","fontSize":"16px","height":"80px"}' class="new5-item-descript line3">{{newsList[3].introduction}}</div>
			  <div :style='{"float":"right","padding":"0 10px","display":"inline-block"}'>
			    <span class="icon iconfont icon-shijian21" :style='{"margin":"0 2px 0 0","lineHeight":"1.5","fontSize":"inherit","color":"inherit","display":"none"}'></span>
			    <span class="text" :style='{"color":"inherit","lineHeight":"1.5","fontSize":"inherit"}'>{{newsList[3].addtime}}</span>
			  </div>
			  <div :style='{"padding":"0 10px","display":"inline-block"}'>
			    <span class="icon iconfont icon-geren16" :style='{"margin":"0 2px 0 0","lineHeight":"1.5","fontSize":"inherit","color":"inherit"}'></span>
			    <span class="text" :style='{"color":"inherit","lineHeight":"1.5","fontSize":"inherit"}'>{{newsList[3].name}}</span>
			  </div>
			  <div :style='{"padding":"0 10px","display":"inline-block"}'>
			    <span class="icon iconfont icon-zan10" :style='{"margin":"0 2px 0 0","lineHeight":"1.5","fontSize":"inherit","color":"inherit"}'></span>
			    <span class="text" :style='{"color":"inherit","lineHeight":"1.5","fontSize":"inherit"}'>{{newsList[3].thumbsupnum}}</span>
			  </div>
			  <div :style='{"padding":"0 10px","display":"inline-block"}'>
			    <span class="icon iconfont icon-shoucang10" :style='{"margin":"0 2px 0 0","lineHeight":"1.5","fontSize":"inherit","color":"inherit"}'></span>
			    <span class="text" :style='{"color":"inherit","lineHeight":"1.5","fontSize":"inherit"}'>{{newsList[3].storeupnum}}</span>
			  </div>
			  <div :style='{"padding":"0 10px","display":"inline-block"}'>
			    <span class="icon iconfont icon-chakan2" :style='{"margin":"0 2px 0 0","lineHeight":"1.5","fontSize":"inherit","color":"inherit"}'></span>
			    <span class="text" :style='{"color":"inherit","lineHeight":"1.5","fontSize":"inherit"}'>{{newsList[3].clicknum}}</span>
			  </div>
			</div>
		  </div>
		</div>
			
			
			
			
			
		











		<div @click="moreBtn('news')" :style='{"border":"0px solid #1d8001","cursor":"pointer","padding":"0 20px 0 0","margin":"20px -12px 0 0","textAlign":"right","display":"block","right":"12%","top":"0","background":"url(http://codegen.caihongy.cn/20231010/b345185c76ac4a77bf4cd6f6171a72ed.png) no-repeat center top / 100% 100%","width":"240px","lineHeight":"73px","position":"absolute","height":"80px"}'>
			<span :style='{"color":"#333","fontSize":"14px"}'>查看更多</span>
			<i :style='{"color":"#333","fontSize":"16px","display":"none"}' class="icon iconfont icon-jiantou09"></i>
		</div>
		
		</div>
	<!-- 新闻资讯 -->



<!-- 特价商品 -->
<div id="animate_listgongxiangdanche" class="lists animate__animated" :style='{"width":"100%","padding":"20px 0 60px","margin":"0px auto 20px","position":"relative","background":"#fff","order":"3"}'>
	<div v-if="false" class="idea" :style='{"padding":"20px","flexWrap":"wrap","background":"#efefef","justifyContent":"space-between","display":"flex"}'>
		<div class="box1" :style='{"width":"20%","background":"#fff","height":"80px"}'></div>
		<div class="box2" :style='{"width":"20%","background":"#fff","height":"80px"}'></div>
		<div class="box3" :style='{"width":"20%","background":"#fff","height":"80px"}'></div>
		<div class="box4" :style='{"width":"20%","background":"#fff","height":"80px"}'></div>
		<div class="box5" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box6" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box7" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box8" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box9" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box10" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
	</div>
	
	<div class="title" :style='{"width":"76%","padding":"40px 0 0","margin":"0px auto","textAlign":"left","background":"url() no-repeat left top / auto 52px","height":"90px"}'>
	  <span :style='{"padding":"0","fontSize":"32px","color":"#000","fontWeight":"600","display":"block","font":"\"宋体\""}'>共享单车展示</span>
	</div>
	
	
	
	
	
	
	
	
	
	






	
		<div v-if="gongxiangdancheList.length" :style='{"padding":"0 12%","color":"#fff","flexWrap":"wrap","background":"none","display":"flex","width":"100%","fontSize":"14px","justifyContent":"space-between","height":"auto"}' class="list list17 index-pv1">
		  <div v-for="item,index in gongxiangdancheList" :key="index"  @click="toDetail('gongxiangdancheDetail', item)" :style='{"cursor":"pointer","margin":"40px 0 0","overflow":"hidden","background":"#fff","width":"31%","position":"relative","height":"480px"}' class="item">
				<img class="image" v-if="preHttp(item.fengmian)" :src="item.fengmian.split(',')[0]" alt="" />
				<img class="image" v-else :src="baseUrl + (item.fengmian?item.fengmian.split(',')[0]:'')" alt="" />
			<div class="content">
		      <div :style='{"color":"#fff","alignItems":"center","display":"none","width":"100%","lineHeight":"24px","fontSize":"14px","textIndent":"2em"}'>{{item.zhaiyao}}</div>
		      <div class="info">
				<div :style='{"margin":"0 0 10px","color":"#fff","textAlign":"left","background":"rgba(0,0,0,0)","width":"100%","lineHeight":"40px","fontSize":"16px"}' class="name ">{{item.biaoti}}</div>
				<div :style='{"margin":"0 0 10px","color":"#fff","textAlign":"left","background":"rgba(0,0,0,0)","width":"100%","lineHeight":"40px","fontSize":"16px"}' class="name ">{{item.bianqian}}</div>
				<div :style='{"width":"100%","padding":"0","margin":"0 10px 0 0","lineHeight":"40px","display":"none"}'>
		          <span class="icon iconfont icon-shijian21" :style='{"margin":"0 2px 0 0","lineHeight":"1.5","fontSize":"inherit","color":"inherit","display":"none"}'></span>
		          <span :style='{"color":"inherit","lineHeight":"1.5","fontSize":"inherit"}'>{{item.addtime}}</span>
		        </div>
		        <div :style='{"padding":"0","margin":"0 10px 0 0","display":"inline-block"}'>
		          <span class="icon iconfont icon-shoucang10" :style='{"margin":"0 2px 0 0","lineHeight":"1.5","fontSize":"inherit","color":"inherit"}'></span>
		          <span :style='{"color":"inherit","lineHeight":"1.5","fontSize":"inherit"}'>{{item.storeupnum}}</span>
		        </div>
		      </div>
		    </div>
		  </div>
		</div>
	
	<div @click="moreBtn('gongxiangdanche')" :style='{"border":"0px solid #1d8001","cursor":"pointer","padding":"0 20px 0 0","margin":"40px -12px 0 0","textAlign":"right","display":"block","right":"12%","top":"0","background":"url(http://codegen.caihongy.cn/20231010/b345185c76ac4a77bf4cd6f6171a72ed.png) no-repeat center top / 100% 100%","width":"240px","lineHeight":"73px","position":"absolute","height":"80px"}'>
		<span :style='{"color":"#333","fontSize":"14px"}'>查看更多</span>
		<i :style='{"color":"#333","fontSize":"16px","display":"none"}' class="icon iconfont icon-jiantou09"></i>
	</div>
	

</div>
<!-- 特价商品 -->
	
</div>
</template>

<script>
import 'animate.css'
import Swiper from "swiper";

  export default {
    //数据集合
    data() {
      return {
        baseUrl: '',
        aboutUsDetail: {},
        systemIntroductionDetail: {},
        newsList: [],

        gongxiangdancheList: [],




      }
    },
    created() {
		this.baseUrl = this.$config.baseUrl;
		this.getNewsList();
		this.getAboutUs();
		this.getSystemIntroduction();
		this.getList();
    },
	mounted() {
		window.addEventListener('scroll', this.handleScroll)
		setTimeout(()=>{
			this.handleScroll()
		},100)
		
		this.swiperChanges()
	},
	beforeDestroy() {
	  window.removeEventListener('scroll', this.handleScroll)
	},
    //方法集合
    methods: {
		swiperChanges() {
			setTimeout(()=>{
			},750)
		},


		handleScroll() {
			let arr = [
				{id:'search',css:'animate__'},
				{id:'about',css:'animate__'},
				{id:'system',css:'animate__'},
				{id:'animate_listgongxiangdanche',css:'animate__'},
				{id:'animate_newsnews',css:'animate__'},
				{id:'msgs',css:'animate__'},
				{id:'friendly',css:'animate__'}
			]
			
			for (let i in arr) {
				let doc = document.getElementById(arr[i].id)
				if (doc) {
					let top = doc.offsetTop
					let win_top = window.innerHeight + window.pageYOffset
					// console.log(top,win_top)
					if (win_top > top && doc.classList.value.indexOf(arr[i].css) < 0) {
						// console.log(doc)
						doc.classList.add(arr[i].css)
					}
				}
			}
		},
      preHttp(str) {
          return str && str.substr(0,4)=='http';
      },
      getAboutUs() {
          this.$http.get('aboutus/detail/1', {}).then(res => {
            if(res.data.code == 0) {
              this.aboutUsDetail = res.data.data;
            }
          })
      },
      getSystemIntroduction() {
          this.$http.get('systemintro/detail/1', {}).then(res => {
            if(res.data.code == 0) {
              this.systemIntroductionDetail = res.data.data;
            }
          })
      },
		getNewsList() {
			let data = {
				page: 1,
				limit: 4,
                sort: 'addtime',
				order: 'desc'
			}
			this.$http.get('news/list', {params: data}).then(res => {
				if (res.data.code == 0) {
					this.newsList = res.data.data.list;
					
					
				}
			});
		},
		getList() {
			let autoSortUrl = "";
			let data = {}
			
			data = {
				page: 1,
				limit: 3,
			}
			this.$http.get('gongxiangdanche/list', {params: data}).then(res => {
				if (res.data.code == 0) {
					this.gongxiangdancheList = res.data.data.list;
					
					// 商品列表样式五
					
				}
			});
		},
		toDetail(path, item) {
			this.$router.push({path: '/index/' + path, query: {id: item.id}});
		},
		moreBtn(path) {
			this.$router.push({path: '/index/' + path});
		}
    }
  }
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.home-preview {
		// -------- search --------
		.search .select /deep/ .el-input__inner {
			border: 0px solid #ddd;
			border-radius: 80px 0 0 80px;
			padding: 0 30px 0 50px;
			box-shadow: 0 0 0px rgba(64, 158, 255, .3);
			outline: none;
			color: #808080;
			background: #f5f5f5;
			width: 180px;
			font-size: 16px;
			height: 60px;
		}
		
		.search .input /deep/ .el-input__inner {
			border: 0px solid #ddd;
			border-radius: 2px;
			padding: 0 10px 0 40px;
			box-shadow: 0 0 0px rgba(64, 158, 255, .3);
			outline: none;
			color: #808080;
			background: url(http://codegen.caihongy.cn/20231010/e6f200cdf25b457cae56c7a886461d70.png) no-repeat 20px center / auto 36px,#f5f5f5;
			width: 380px;
			font-size: 16px;
			height: 60px;
		}
		// -------- search --------
		.recommend {
			.list3 .swiper-button-prev {
				left: 10px;
				right: auto;
			}
			
			.list3 .swiper-button-prev::after {
				color: #0c5f62;
			}
			
			.list3 .swiper-button-next {
				left: auto;
				right: 10px;
			}
			
			.list3 .swiper-button-next::after {
				color: #0c5f62;
			}
			
			.list5 .swiper-button-prev {
				left: 10px;
				right: auto;
			}
			
			.list5 .swiper-button-prev::after {
				color: rgb(64, 158, 255);
        }
        
        .list5 .swiper-button-next {
				left: auto;
				right: 10px;
			}
			
			.list5 .swiper-button-next::after {
				color: rgb(64, 158, 255);
			}
			
			.list5 {
				.swiper-slide-prev {
					position: relative;
					z-index: 3;
				}
		
				.swiper-slide-next {
					position: relative;
					z-index: 3;
				}
		
				.swiper-slide-active {
					position: relative;
					z-index: 5;
				}
			}
			
			.index-pv1 .animation-box {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				z-index: initial;
			}
			
			.index-pv1 .animation-box:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, -10px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
			}
			
			.index-pv1 .animation-box img {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
			}
			
			.index-pv1 .animation-box img:hover {
				transform: rotate(0deg) scale(1.02) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
		}
		
		.news {
			.list3 .swiper-button-prev {
				left: 10px;
				right: auto;
			}
			
			.list3 .swiper-button-prev::after {
				color: rgb(64, 158, 255);
			}
			
			.list3 .swiper-button-next {
				left: auto;
				right: 10px;
			}
			
			.list3 .swiper-button-next::after {
				color: rgb(64, 158, 255);
			}
			
			.list6 .swiper-button-prev {
				left: 10px;
				right: auto;
			}
			
			.list6 .swiper-button-prev::after {
				color: rgb(64, 158, 255);
			}
			
			.list6 .swiper-button-next {
				left: auto;
				right: 10px;
			}
			
			.list6 .swiper-button-next::after {
				color: rgb(64, 158, 255);
			}
			
			.index-pv1 .animation-box {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				z-index: initial;
			}
			
			.index-pv1 .animation-box:hover {
				transform: rotate(0deg) scale(0.96) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
			}
			
			.index-pv1 .animation-box img {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
			}
			
			.index-pv1 .animation-box img:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
		}
	
		.lists {
			.list3 .swiper-button-prev {
				left: 10px;
				right: auto;
			}
			
			.list3 .swiper-button-prev::after {
				color: rgb(64, 158, 255);
			}
			
			.list3 .swiper-button-next {
				left: auto;
				right: 10px;
        }
        
        .list3 .swiper-button-next::after {
				color: rgb(64, 158, 255);
			}
			
			.list5 .swiper-button-prev {
				left: 10px;
				right: auto;
			}
			
			.list5 .swiper-button-prev::after {
				color: rgb(64, 158, 255);
			}
			
			.list5 .swiper-button-next {
            left: auto;
            right: 10px;
			}
			
			.list5 .swiper-button-next::after {
				color: rgb(64, 158, 255);
			}
			
			.list5 {
				.swiper-slide-prev {
					position: relative;
					z-index: 3;
				}
		
				.swiper-slide-next {
					position: relative;
					z-index: 3;
				}
		
				.swiper-slide-active {
					position: relative;
					z-index: 5;
				}
			}
			
			.index-pv1 .animation-box {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				z-index: initial;
			}
			
			.index-pv1 .animation-box:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, -10px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
			}
			
			.index-pv1 .animation-box img {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
			}
			
			.index-pv1 .animation-box img:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
		}
	}
	








	.home-preview .recommend .list16 .list-item {
				cursor: pointer;
				padding: 0px;
				margin: 0 0 40px 0;
				background: #fff;
				display: flex;
				width: 23%;
				font-size: 0;
				position: relative;
				flex-wrap: wrap;
				height: auto;
			}
	
	.home-preview .recommend .list16 .list-item:hover {
				background: #3795c4;
			}
	
	.home-preview .recommend .list16 .list-item .title {
				padding: 0 10px;
				overflow: hidden;
				color: #333;
				white-space: nowrap;
				width: 100%;
				font-size: 16px;
				border-color: red;
				border-width: 0;
				line-height: 36px;
				text-overflow: ellipsis;
				border-style: solid;
			}
	
	.home-preview .recommend .list16 .list-item:hover .title {
				color: #fff;
			}
	
	.home-preview .recommend .list16 .list-item .time .icon {
				margin: 0 2px 0 0;
				color: inherit;
				font-size: 14px;
				line-height: 28px;
			}
	.home-preview .recommend .list16 .list-item:hover .time .icon {
				color: #fff;
			}
	.home-preview .recommend .list16 .list-item .time .text {
				color: inherit;
				font-size: 14px;
				line-height: 28px;
			}
	.home-preview .recommend .list16 .list-item:hover .time .text {
				color: #fff;
			}
	
	.home-preview .recommend .list16 .list-item .publisher .icon {
				margin: 0 2px 0 0;
				color: inherit;
				font-size: 14px;
				line-height: 28px;
			}
	.home-preview .recommend .list16 .list-item:hover .publisher .icon {
				color: #fff;
			}
	.home-preview .recommend .list16 .list-item .publisher .text {
				color: inherit;
				font-size: 14px;
				line-height: 28px;
			}
	.home-preview .recommend .list16 .list-item:hover .publisher .text {
				color: #fff;
			}
	
	.home-preview .recommend .list16 .list-item .like .icon {
				margin: 0 2px 0 0;
				color: inherit;
				font-size: 14px;
				line-height: 28px;
			}
	.home-preview .recommend .list16 .list-item:hover .like .icon {
				color: #fff;
			}
	.home-preview .recommend .list16 .list-item .like .text {
				color: inherit;
				font-size: 14px;
				line-height: 28px;
			}
	.home-preview .recommend .list16 .list-item:hover .like .text {
				color: #fff;
			}
	
	.home-preview .recommend .list16 .list-item .collect .icon {
				margin: 0 2px 0 0;
				color: inherit;
				font-size: 14px;
				line-height: 28px;
			}
	.home-preview .recommend .list16 .list-item:hover .collect .icon {
				color: #fff;
			}
	.home-preview .recommend .list16 .list-item .collect .text {
				color: inherit;
				font-size: 14px;
				line-height: 28px;
			}
	.home-preview .recommend .list16 .list-item:hover .collect .text {
				color: #fff;
			}
	
	.home-preview .recommend .list16 .list-item .view .icon {
				margin: 0 2px 0 0;
				color: inherit;
				font-size: 14px;
				line-height: 28px;
			}
	.home-preview .recommend .list16 .list-item:hover .view .icon {
				color: #fff;
			}
	.home-preview .recommend .list16 .list-item .view .text {
				color: inherit;
				font-size: 14px;
				line-height: 28px;
			}
	.home-preview .recommend .list16 .list-item:hover .view .text {
				color: #fff;
			}
	
	.home-preview .recommend .list16 .list-item .desc {
				color: #666;
				display: none;
				font-size: 12px;
				line-height: 1.5;
			}
	.home-preview .recommend .list16 .list-item:hover .desc {
				color: #fff;
			}


	.home-preview .lists .list17 .item .image {
				object-fit: cover;
				display: block;
				width: 100%;
				transition: 0.3s;
				height: 100%;
			}

	.home-preview .lists .list17 .item:hover .image {
				transform: scale(1);
			}
	
	.home-preview .lists .list17 .item .content {
				padding: 20px;
				left: 0;
				bottom: -100%;
				background: rgba(34,81,106,.6);
				display: flex;
				width: 100%;
				position: absolute;
				flex-wrap: wrap;
				transition: 0.3s;
				height: 100%;
			}
	
	.home-preview .lists .list17 .item:hover .content {
				bottom: 0;
			}
</style>
