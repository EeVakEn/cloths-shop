module.exports = {
  runtimeCompiler: true,
  devServer:{
    proxy: "http://integration.cdek.ru/",
  },
  css: {
    loaderOptions: {
      sass: {
        additionalData: `
                @import "@/assets/styles/variables.scss";
                `
      }
    }
  }
}


