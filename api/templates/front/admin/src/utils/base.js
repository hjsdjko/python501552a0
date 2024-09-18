const base = {
    get() {
        return {
            url : "http://localhost:8080/python501552a0/",
            name: "python501552a0",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/front/dist/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "基于Spark的共享单车数据存储系统的设计与实现"
        } 
    }
}
export default base
