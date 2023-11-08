import { Module } from "@nestjs/common";
import { ProductModuleBase } from "./base/product.module.base";
import { ProductService } from "./product.service";
import { ProductController } from "./product.controller";
import { ProductResolver } from "./product.resolver";

@Module({
  imports: [ProductModuleBase],
  controllers: [ProductController],
  providers: [ProductService, ProductResolver],
  exports: [ProductService],
})
export class ProductModule {}
