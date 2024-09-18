<template>
	<div class="addEdit-block" :style='{"padding":"0px 0px 30px","fontSize":"14px","color":"#000","background":"none"}'>
		<el-form
			:style='{"border":"0px solid rgba(255,255,255,1)","padding":"30px 0 10px","borderRadius":"0 0 8px 8px","alignItems":"flex-start","flexWrap":"wrap","background":"rgba(255,255,255,0)","display":"flex","fontSize":"inherit"}'
			class="add-update-preview"
			ref="ruleForm"
			:model="ruleForm"
			:rules="rules"
			label-width="150px"
		>
			<template >
				<el-form-item :style='{"width":"48%","margin":"0 0 30px 0","fontSize":"inherit","color":"inherit"}' class="input" v-if="type!='info'"  label="标题" prop="biaoti">
					<el-input v-model="ruleForm.biaoti"  placeholder="标题" clearable  :readonly="ro.biaoti"></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"48%","margin":"0 0 30px 0","fontSize":"inherit","color":"inherit"}' v-else class="input" label="标题" prop="biaoti">
					<el-input v-model="ruleForm.biaoti" placeholder="标题" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"48%","margin":"0 0 30px 0","fontSize":"inherit","color":"inherit"}' class="upload" v-if="type!='info' && !ro.fengmian" label="封面" prop="fengmian">
					<file-upload
						tip="点击上传封面"
						action="file/upload"
						:limit="3"
						:multiple="true"
						:fileUrls="ruleForm.fengmian?ruleForm.fengmian:''"
						@change="fengmianUploadChange"
					></file-upload>
				</el-form-item>
				<el-form-item :style='{"width":"48%","margin":"0 0 30px 0","fontSize":"inherit","color":"inherit"}' class="upload" v-else-if="ruleForm.fengmian" label="封面" prop="fengmian">
					<img v-if="ruleForm.fengmian.substring(0,4)=='http'" class="upload-img" style="margin-right:20px;" v-bind:key="index" :src="ruleForm.fengmian.split(',')[0]" width="100" height="100">
					<img v-else class="upload-img" style="margin-right:20px;" v-bind:key="index" v-for="(item,index) in ruleForm.fengmian.split(',')" :src="$base.url+item" width="100" height="100">
				</el-form-item>
				<el-form-item :style='{"width":"48%","margin":"0 0 30px 0","fontSize":"inherit","color":"inherit"}' class="input" v-if="type!='info'"  label="便签" prop="bianqian">
					<el-input v-model="ruleForm.bianqian"  placeholder="便签" clearable  :readonly="ro.bianqian"></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"48%","margin":"0 0 30px 0","fontSize":"inherit","color":"inherit"}' v-else class="input" label="便签" prop="bianqian">
					<el-input v-model="ruleForm.bianqian" placeholder="便签" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"48%","margin":"0 0 30px 0","fontSize":"inherit","color":"inherit"}' class="input" v-if="type!='info'"  label="作者" prop="zuozhe">
					<el-input v-model="ruleForm.zuozhe"  placeholder="作者" clearable  :readonly="ro.zuozhe"></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"48%","margin":"0 0 30px 0","fontSize":"inherit","color":"inherit"}' v-else class="input" label="作者" prop="zuozhe">
					<el-input v-model="ruleForm.zuozhe" placeholder="作者" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"48%","margin":"0 0 30px 0","fontSize":"inherit","color":"inherit"}' class="input" v-if="type!='info'"  label="浏览量" prop="liulanliang">
					<el-input-number v-model="ruleForm.liulanliang" placeholder="浏览量" :readonly="ro.liulanliang"></el-input-number>
				</el-form-item>
				<el-form-item :style='{"width":"48%","margin":"0 0 30px 0","fontSize":"inherit","color":"inherit"}' v-else class="input" label="浏览量" prop="liulanliang">
					<el-input v-model="ruleForm.liulanliang" placeholder="浏览量" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"48%","margin":"0 0 30px 0","fontSize":"inherit","color":"inherit"}' class="input" v-if="type!='info'"  label="反对数" prop="fanduishu">
					<el-input-number v-model="ruleForm.fanduishu" placeholder="反对数" :readonly="ro.fanduishu"></el-input-number>
				</el-form-item>
				<el-form-item :style='{"width":"48%","margin":"0 0 30px 0","fontSize":"inherit","color":"inherit"}' v-else class="input" label="反对数" prop="fanduishu">
					<el-input v-model="ruleForm.fanduishu" placeholder="反对数" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"48%","margin":"0 0 30px 0","fontSize":"inherit","color":"inherit"}' class="input" v-if="type!='info'"  label="点赞数" prop="dianzanshu">
					<el-input-number v-model="ruleForm.dianzanshu" placeholder="点赞数" :readonly="ro.dianzanshu"></el-input-number>
				</el-form-item>
				<el-form-item :style='{"width":"48%","margin":"0 0 30px 0","fontSize":"inherit","color":"inherit"}' v-else class="input" label="点赞数" prop="dianzanshu">
					<el-input v-model="ruleForm.dianzanshu" placeholder="点赞数" readonly></el-input>
				</el-form-item>
			</template>
				<el-form-item :style='{"width":"48%","margin":"0 0 30px 0","fontSize":"inherit","color":"inherit"}' class="textarea" v-if="type!='info'" label="摘要" prop="zhaiyao">
					<el-input
					  style="min-width: 200px; max-width: 600px;"
					  type="textarea"
					  :rows="8"
					  placeholder="摘要"
					  v-model="ruleForm.zhaiyao" >
					</el-input>
				</el-form-item>
				<el-form-item :style='{"width":"48%","margin":"0 0 30px 0","fontSize":"inherit","color":"inherit"}' v-else-if="ruleForm.zhaiyao" label="摘要" prop="zhaiyao">
					<span :style='{"padding":"0 20px","color":"inherit","background":"#fff","display":"inline-block","width":"80%","fontSize":"14px","lineHeight":"40px","fontWeight":"500"}'>{{ruleForm.zhaiyao}}</span>
				</el-form-item>
				<el-form-item :style='{"width":"48%","margin":"0 0 30px 0","fontSize":"inherit","color":"inherit"}' v-if="type!='info'"  label="详情" prop="detail">
					<editor 
						style="min-width: 200px; max-width: 600px;"
						v-model="ruleForm.detail" 
						class="editor" 
						action="file/upload">
					</editor>
				</el-form-item>
				<el-form-item :style='{"width":"48%","margin":"0 0 30px 0","fontSize":"inherit","color":"inherit"}' v-else-if="ruleForm.detail" label="详情" prop="detail">
                    <span :style='{"padding":"0 20px","color":"inherit","background":"#fff","display":"inline-block","width":"80%","fontSize":"14px","lineHeight":"40px","fontWeight":"500"}' v-html="ruleForm.detail"></span>
                </el-form-item>
			<el-form-item :style='{"padding":"0 10px","margin":"30px 0","alignItems":"center","textAlign":"center","display":"flex","width":"100%","perspective":"320px","-webkitPerspective":"320px","fontSize":"48px","justifyContent":"flex-end"}' class="btn">
				<el-button class="btn3"  v-if="type!='info'" type="success" @click="onSubmit">
					<span class="icon iconfont icon-tijiao16" :style='{"margin":"0 2px","fontSize":"18px","color":"inherit","display":"none"}'></span>
					提交
				</el-button>
				<el-button class="btn4" v-if="type!='info'" type="success" @click="back()">
					<span class="icon iconfont icon-quxiao09" :style='{"margin":"0 2px","fontSize":"18px","color":"inherit","display":"none"}'></span>
					取消
				</el-button>
				<el-button class="btn5" v-if="type=='info'" type="success" @click="back()">
					<span class="icon iconfont icon-fanhui01" :style='{"margin":"0 2px","fontSize":"18px","color":"inherit","display":"none"}'></span>
					返回
				</el-button>
			</el-form-item>
		</el-form>
    

  </div>
</template>
<script>
// 数字，邮件，手机，url，身份证校验
import { isNumber,isIntNumer,isEmail,isPhone, isMobile,isURL,checkIdCard } from "@/utils/validate";
export default {
	data() {
		let self = this
		var validateIdCard = (rule, value, callback) => {
			if(!value){
				callback();
			} else if (!checkIdCard(value)) {
				callback(new Error("请输入正确的身份证号码"));
			} else {
				callback();
			}
		};
		var validateUrl = (rule, value, callback) => {
			if(!value){
				callback();
			} else if (!isURL(value)) {
				callback(new Error("请输入正确的URL地址"));
			} else {
				callback();
			}
		};
		var validateMobile = (rule, value, callback) => {
			if(!value){
				callback();
			} else if (!isMobile(value)) {
				callback(new Error("请输入正确的手机号码"));
			} else {
				callback();
			}
		};
		var validatePhone = (rule, value, callback) => {
			if(!value){
				callback();
			} else if (!isPhone(value)) {
				callback(new Error("请输入正确的电话号码"));
			} else {
				callback();
			}
		};
		var validateEmail = (rule, value, callback) => {
			if(!value){
				callback();
			} else if (!isEmail(value)) {
				callback(new Error("请输入正确的邮箱地址"));
			} else {
				callback();
			}
		};
		var validateNumber = (rule, value, callback) => {
			if(!value){
				callback();
			} else if (!isNumber(value)) {
				callback(new Error("请输入数字"));
			} else {
				callback();
			}
		};
		var validateIntNumber = (rule, value, callback) => {
			if(!value){
				callback();
			} else if (!isIntNumer(value)) {
				callback(new Error("请输入整数"));
			} else {
				callback();
			}
		};
		return {
			id: '',
			type: '',
			
			
			ro:{
				biaoti : false,
				fengmian : false,
				bianqian : false,
				zuozhe : false,
				liulanliang : false,
				zhaiyao : false,
				fanduishu : false,
				dianzanshu : false,
				detail : false,
				discussnum : false,
				storeupnum : false,
			},
			
			
			ruleForm: {
				biaoti: '',
				fengmian: '',
				bianqian: '',
				zuozhe: '',
				liulanliang: '',
				zhaiyao: '',
				fanduishu: '',
				dianzanshu: '',
				detail: '',
			},
		

			
			rules: {
				biaoti: [
				],
				fengmian: [
				],
				bianqian: [
				],
				zuozhe: [
				],
				liulanliang: [
					{ validator: validateNumber, trigger: 'blur' },
				],
				zhaiyao: [
				],
				fanduishu: [
					{ validator: validateNumber, trigger: 'blur' },
				],
				dianzanshu: [
					{ validator: validateNumber, trigger: 'blur' },
				],
				detail: [
				],
				discussnum: [
					{ validator: validateIntNumber, trigger: 'blur' },
				],
				storeupnum: [
					{ validator: validateIntNumber, trigger: 'blur' },
				],
			}
		};
	},
	props: ["parent"],
	computed: {



	},
    components: {
    },
	created() {
	},
	methods: {
		
		// 下载
		download(file){
			window.open(`${file}`)
		},
		// 初始化
		init(id,type) {
			if (id) {
				this.id = id;
				this.type = type;
			}
			if(this.type=='info'||this.type=='else'){
				this.info(id);
			}else if(this.type=='logistics'){
				this.logistics=false;
				this.info(id);
			}else if(this.type=='cross'){
				var obj = this.$storage.getObj('crossObj');
				for (var o in obj){
						if(o=='biaoti'){
							this.ruleForm.biaoti = obj[o];
							this.ro.biaoti = true;
							continue;
						}
						if(o=='fengmian'){
							this.ruleForm.fengmian = obj[o];
							this.ro.fengmian = true;
							continue;
						}
						if(o=='bianqian'){
							this.ruleForm.bianqian = obj[o];
							this.ro.bianqian = true;
							continue;
						}
						if(o=='zuozhe'){
							this.ruleForm.zuozhe = obj[o];
							this.ro.zuozhe = true;
							continue;
						}
						if(o=='liulanliang'){
							this.ruleForm.liulanliang = obj[o];
							this.ro.liulanliang = true;
							continue;
						}
						if(o=='zhaiyao'){
							this.ruleForm.zhaiyao = obj[o];
							this.ro.zhaiyao = true;
							continue;
						}
						if(o=='fanduishu'){
							this.ruleForm.fanduishu = obj[o];
							this.ro.fanduishu = true;
							continue;
						}
						if(o=='dianzanshu'){
							this.ruleForm.dianzanshu = obj[o];
							this.ro.dianzanshu = true;
							continue;
						}
						if(o=='detail'){
							this.ruleForm.detail = obj[o];
							this.ro.detail = true;
							continue;
						}
						if(o=='discussnum'){
							this.ruleForm.discussnum = obj[o];
							this.ro.discussnum = true;
							continue;
						}
						if(o=='storeupnum'){
							this.ruleForm.storeupnum = obj[o];
							this.ro.storeupnum = true;
							continue;
						}
				}
				











			}
			
			
			
		},
    // 多级联动参数

    info(id) {
      this.$http({
        url: `gongxiangdanche/info/${id}`,
        method: "get"
      }).then(({ data }) => {
        if (data && data.code === 0) {
        this.ruleForm = data.data;
        //解决前台上传图片后台不显示的问题
        let reg=new RegExp('../../../upload','g')//g代表全部
        this.ruleForm.detail = this.ruleForm.detail.replace(reg,'../../../python501552a0/upload');
        } else {
          this.$message.error(data.msg);
        }
      });
    },


    // 提交
    onSubmit() {


	if(this.ruleForm.fengmian!=null) {
		this.ruleForm.fengmian = this.ruleForm.fengmian.replace(new RegExp(this.$base.url,"g"),"");
	}










var objcross = this.$storage.getObj('crossObj');
      //更新跨表属性
       var crossuserid;
       var crossrefid;
       var crossoptnum;
       if(this.type=='cross'){
                var statusColumnName = this.$storage.get('statusColumnName');
                var statusColumnValue = this.$storage.get('statusColumnValue');
                if(statusColumnName!='') {
                        var obj = this.$storage.getObj('crossObj');
                       if(statusColumnName && !statusColumnName.startsWith("[")) {
                               for (var o in obj){
                                 if(o==statusColumnName){
                                   obj[o] = statusColumnValue;
                                 }
                               }
                               var table = this.$storage.get('crossTable');
                             this.$http({
                                 url: `${table}/update`,
                                 method: "post",
                                 data: obj
                               }).then(({ data }) => {});
                       } else {
                               crossuserid=this.$storage.get('userid');
                               crossrefid=obj['id'];
                               crossoptnum=this.$storage.get('statusColumnName');
                               crossoptnum=crossoptnum.replace(/\[/,"").replace(/\]/,"");
                        }
                }
        }
		this.$refs["ruleForm"].validate(valid => {
			if (valid) {
				if(crossrefid && crossuserid) {
					this.ruleForm.crossuserid = crossuserid;
					this.ruleForm.crossrefid = crossrefid;
					let params = { 
						page: 1, 
						limit: 10, 
						crossuserid:this.ruleForm.crossuserid,
						crossrefid:this.ruleForm.crossrefid,
					} 
				this.$http({ 
					url: "gongxiangdanche/page", 
					method: "get", 
					params: params 
				}).then(({ 
					data 
				}) => { 
					if (data && data.code === 0) { 
						if(data.data.total>=crossoptnum) {
							this.$message.error(this.$storage.get('tips'));
							return false;
						} else {
							this.$http({
								url: `gongxiangdanche/${!this.ruleForm.id ? "save" : "update"}`,
								method: "post",
								data: this.ruleForm
							}).then(({ data }) => {
								if (data && data.code === 0) {
									this.$message({
										message: "操作成功",
										type: "success",
										duration: 1500,
										onClose: () => {
											this.parent.showFlag = true;
											this.parent.addOrUpdateFlag = false;
											this.parent.gongxiangdancheCrossAddOrUpdateFlag = false;
											this.parent.search();
											this.parent.contentStyleChange();
										}
									});
								} else {
									this.$message.error(data.msg);
								}
							});

						}
					} else { 
				} 
			});
		} else {
			this.$http({
				url: `gongxiangdanche/${!this.ruleForm.id ? "save" : "update"}`,
				method: "post",
			   data: this.ruleForm
			}).then(({ data }) => {
				if (data && data.code === 0) {
					this.$message({
						message: "操作成功",
						type: "success",
						duration: 1500,
						onClose: () => {
							this.parent.showFlag = true;
							this.parent.addOrUpdateFlag = false;
							this.parent.gongxiangdancheCrossAddOrUpdateFlag = false;
							this.parent.search();
							this.parent.contentStyleChange();
						}
					});
				} else {
					this.$message.error(data.msg);
			   }
			});
		 }
         }
       });
    },
    // 获取uuid
    getUUID () {
      return new Date().getTime();
    },
    // 返回
    back() {
      this.parent.showFlag = true;
      this.parent.addOrUpdateFlag = false;
      this.parent.gongxiangdancheCrossAddOrUpdateFlag = false;
      this.parent.contentStyleChange();
    },
    fengmianUploadChange(fileUrls) {
	    this.ruleForm.fengmian = fileUrls;
    },
  }
};
</script>
<style lang="scss" scoped>
	.amap-wrapper {
		width: 100%;
		height: 500px;
	}
	
	.search-box {
		position: absolute;
	}
	
	.el-date-editor.el-input {
		width: auto;
	}
	
	.add-update-preview .el-form-item /deep/ .el-form-item__label {
	  	  padding: 0 10px 0 0;
	  	  color: #999;
	  	  font-weight: 500;
	  	  display: inline-block;
	  	  width: 150px;
	  	  font-size: inherit;
	  	  line-height: 40px;
	  	  text-align: right;
	  	}
	
	.add-update-preview .el-form-item /deep/ .el-form-item__content {
	  margin-left: 150px;
	}
	
	.add-update-preview .el-input /deep/ .el-input__inner {
	  	  border: 0px solid #000;
	  	  border-radius: 0px;
	  	  padding: 0 12px;
	  	  box-shadow: 0 0 0px rgba(64, 158, 255, .5);
	  	  outline: none;
	  	  color: inherit;
	  	  background: #fff;
	  	  width: auto;
	  	  font-size: 14px;
	  	  min-width: 350px;
	  	  height: 36px;
	  	}
	.add-update-preview .el-input-number /deep/ .el-input__inner {
		text-align: left;
	  	  border: 0px solid #000;
	  	  border-radius: 0px;
	  	  padding: 0 12px;
	  	  box-shadow: 0 0 0px rgba(64, 158, 255, .5);
	  	  outline: none;
	  	  color: inherit;
	  	  background: #fff;
	  	  width: auto;
	  	  font-size: 14px;
	  	  min-width: 350px;
	  	  height: 36px;
	  	}
	.add-update-preview .el-input-number /deep/ .el-input-number__decrease {
		display: none;
	}
	.add-update-preview .el-input-number /deep/ .el-input-number__increase {
		display: none;
	}
	
	.add-update-preview .el-select /deep/ .el-input__inner {
	  	  border: 0px solid #000;
	  	  border-radius: 0px;
	  	  padding: 0 10px;
	  	  box-shadow: 0 0 0px rgba(64, 158, 255, .5);
	  	  outline: none;
	  	  color: inherit;
	  	  background: #fff;
	  	  width: auto;
	  	  font-size: 14px;
	  	  min-width: 350px;
	  	  height: 36px;
	  	}
	
	.add-update-preview .el-date-editor /deep/ .el-input__inner {
	  	  border: 0px solid #000;
	  	  border-radius: 0px;
	  	  padding: 0 10px 0 30px;
	  	  box-shadow: 0 0 0px rgba(64, 158, 255, .5);
	  	  outline: none;
	  	  color: inherit;
	  	  background: #fff;
	  	  width: auto;
	  	  font-size: 14px;
	  	  min-width: 350px;
	  	  height: 36px;
	  	}
	
	.add-update-preview /deep/ .el-upload--picture-card {
		background: transparent;
		border: 0;
		border-radius: 0;
		width: auto;
		height: auto;
		line-height: initial;
		vertical-align: middle;
	}
	
	.add-update-preview /deep/ .upload .upload-img {
	  	  border: 0px solid #000;
	  	  cursor: pointer;
	  	  border-radius: 0px;
	  	  color: inherit;
	  	  background: #fff;
	  	  object-fit: cover;
	  	  width: 180px;
	  	  font-size: 32px;
	  	  line-height: 90px;
	  	  text-align: center;
	  	  height: 90px;
	  	}
	
	.add-update-preview /deep/ .el-upload-list .el-upload-list__item {
	  	  border: 0px solid #000;
	  	  cursor: pointer;
	  	  border-radius: 0px;
	  	  color: inherit;
	  	  background: #fff;
	  	  object-fit: cover;
	  	  width: 180px;
	  	  font-size: 32px;
	  	  line-height: 90px;
	  	  text-align: center;
	  	  height: 90px;
	  	}
	
	.add-update-preview /deep/ .el-upload .el-icon-plus {
	  	  border: 0px solid #000;
	  	  cursor: pointer;
	  	  border-radius: 0px;
	  	  color: inherit;
	  	  background: #fff;
	  	  object-fit: cover;
	  	  width: 180px;
	  	  font-size: 32px;
	  	  line-height: 90px;
	  	  text-align: center;
	  	  height: 90px;
	  	}
	
	.add-update-preview .el-textarea /deep/ .el-textarea__inner {
	  	  border: 0px solid #000;
	  	  border-radius: 0px;
	  	  padding: 12px;
	  	  box-shadow: 0 0 0px rgba(64, 158, 255, .5);
	  	  outline: none;
	  	  color: inherit;
	  	  background: #fff;
	  	  width: auto;
	  	  font-size: 14px;
	  	  min-width: 350px;
	  	  height: 120px;
	  	}
	
	.add-update-preview .btn .btn1 {
				border: 0px solid rgba(126, 96, 16, .2);
				cursor: pointer;
				padding: 0 30px;
				margin: 0px 20px 0 0;
				color: #fff;
				display: inline-block;
				font-size: 14px;
				line-height: 24px;
				border-radius: 4px;
				outline: none;
				background: #62779c;
				width: auto;
				height: 40px;
			}
	
	.add-update-preview .btn .btn1:hover {
				transform: scale(0.9);
				opacity: 0.8;
			}
	
	.add-update-preview .btn .btn2 {
				border: 0px solid rgba(126, 96, 16, .2);
				cursor: pointer;
				border-radius: 4px;
				padding: 0 30px;
				margin: 0px 20px 0 0;
				outline: none;
				color: #fff;
				background: #62779c;
				width: auto;
				font-size: 14px;
				line-height: 24px;
				height: 40px;
			}
	
	.add-update-preview .btn .btn2:hover {
				transform: scale(0.9);
				opacity: 0.8;
			}
	
	.add-update-preview .btn .btn3 {
				border: 0px solid rgba(126, 96, 16, .2);
				cursor: pointer;
				border-radius: 4px;
				padding: 0 30px;
				margin: 0px 20px 0 0;
				outline: none;
				color: #fff;
				background: #62779c;
				width: auto;
				font-size: 16px;
				line-height: 24px;
				height: 40px;
			}
	
	.add-update-preview .btn .btn3:hover {
				transform: scale(0.9);
				opacity: 0.8;
			}
	
	.add-update-preview .btn .btn4 {
				border: 0px solid rgba(126, 96, 16, .2);
				cursor: pointer;
				border-radius: 4px;
				padding: 0 30px;
				margin: 0px 20px 0 0;
				outline: none;
				color: #fff;
				background: #62779c;
				width: auto;
				font-size: 16px;
				line-height: 24px;
				height: 40px;
			}
	
	.add-update-preview .btn .btn4:hover {
				transform: scale(0.9);
				opacity: 0.8;
			}
	
	.add-update-preview .btn .btn5 {
				border: 0px solid rgba(126, 96, 16, .2);
				cursor: pointer;
				border-radius: 4px;
				padding: 0 30px;
				margin: 0px 20px 0 0;
				outline: none;
				color: #fff;
				background: #62779c;
				width: auto;
				font-size: 16px;
				line-height: 24px;
				height: 40px;
			}
	
	.add-update-preview .btn .btn5:hover {
				transform: scale(0.9);
				opacity: 0.8;
			}
</style>
