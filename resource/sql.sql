create table lagoudata
(
  short_name          varchar(255) not null comment '公司简称',
  full_name           varchar(255) not null comment '公司全称',
  company_link        varchar(255) null comment '公司网址',
  company_logo        varchar(255) null comment '公司图片',
  company_word        varchar(255) null comment '公司口号',
  company_type        varchar(255) null comment '公司行业',
  company_process     varchar(255) null comment '公司发展',
  company_number      varchar(100) null comment '公司人数',
  company_address     varchar(255) null comment '公司地址',
  company_detail      text         null comment '公司介绍',
  company_products    longtext     null comment '公司产品',
  company_managers    longtext     null comment '公司管理团队',
  company_jobs        longtext     null comment '公司招聘职位',
  company_history     longtext     null comment '发展历程',
  resume_process_rate varchar(255) null comment '简历及时处理率',
  interview_com_num   varchar(100) null comment '面试评价个数（个）',
  score               varchar(255) null comment '综合评分（总分5.0分）',
  id                  varchar(100) not null comment 'id'
    primary key,
  time                varchar(100) null comment '时间'
);

