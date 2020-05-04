# main.py
import sys
import json
if __name__ == "__main__":
        #!/usr/bin/env python
        # coding: utf-8

        # In[22]:


        # # enanle print everywhere
        # from IPython.core.interactiveshell import InteractiveShell
        # InteractiveShell.ast_node_interactivity = "all"


        # In[23]:


        # Module name, and data content
        name = sys.argv[1]
        name = name.lower()
        entity_name = name.capitalize()
        # Json


        # # Generates module, controller, service

        # In[40]:


        # if next cell print nest: command not found, execute this
        # !npm install -g @nestjs/cli


        # In[41]:


        get_ipython().system(' nest g module ./modules/$name')
        get_ipython().system(' nest g controller ./modules/$name')
        get_ipython().system(' nest g service ./modules/$name')


        # #  Create entity file

        # In[42]:


        # In[43]:


        with open(f'{sys.argv[2]}', 'r') as file:
            test_load = json.load(file)
        test_load


        # In[44]:


        colums = []
        for x in test_load:
            if type(test_load[x]) == str:
                colums.append(f"\n\n  @Column()\n  @ApiModelProperty()\n  {x}: string;")
            if type(test_load[x]) == int:
                colums.append(f"\n\n  @Column()\n  @ApiModelProperty()\n  {x}: number;")
            if type(test_load[x]) == bool:
                colums.append(f"\n\n  @Column()\n  @ApiModelProperty()\n  {x}: boolean;")
        #reconstruct list to string
        colums = ''.join(colums)
        colums


        # In[45]:


        entity = '''
        import { Entity, PrimaryGeneratedColumn, Column } from 'typeorm';
        import { ApiModelProperty } from '@nestjs/swagger';
        @Entity()
        export class %s {
          @PrimaryGeneratedColumn()
          @ApiModelProperty()
          id: number;%s
        }
        '''% (entity_name, colums)
        with open(f'./src/modules/{name}/{name}.entity.ts', 'w') as file: # Use file to refer to the file object
            file.write(entity)



        # # Import created entity to module 配置数据库

        # In[46]:


        module = '''
        import { Module } from '@nestjs/common';
        import { TypeOrmModule } from '@nestjs/typeorm';
        import { %s } from './%s.entity';
        import { %sController } from './%s.controller';
        import { %sService } from './%s.service';

        @Module({
          imports: [
            TypeOrmModule.forFeature([%s])],
          controllers: [%sController],
          providers: [%sService]
        })
        export class %sModule {}

        '''% (entity_name, name, entity_name,name, entity_name, name, entity_name, entity_name, entity_name, entity_name)

        with open(f'./src/modules/{name}/{name}.module.ts', 'w') as file: # Use file to refer to the file object
            file.write(module)



        # # Regenerate controller with crud

        # In[47]:


        controller = '''
        import { Controller } from '@nestjs/common';
        import { Crud, CrudController } from '@nestjsx/crud';
        import { %s } from './%s.entity';
        import { %sService } from './%s.service';
        import { ApiUseTags } from '@nestjs/swagger';

        @Crud({
          model: {
            type: %s,
          },
        })
        @Controller('%s')
        @ApiUseTags('%s')
        export class %sController implements CrudController<%s> {
          constructor(public service: %sService) {}
        }
        ''' %(entity_name, name, entity_name, name, entity_name, name, entity_name, entity_name, entity_name, entity_name)
        with open(f'./src/modules/{name}/{name}.controller.ts', 'w') as file: # Use file to refer to the file object
            file.write(controller)



        # In[48]:


        service = '''
        import { Injectable } from '@nestjs/common';
        import { %s } from './%s.entity';
        import { InjectRepository } from '@nestjs/typeorm';
        import { TypeOrmCrudService } from '@nestjsx/crud-typeorm';

        @Injectable()
        export class %sService extends TypeOrmCrudService<%s> {
          constructor(@InjectRepository(%s) repo) {
            super(repo);
          }
        }

        '''%(entity_name, name, entity_name, entity_name, entity_name)
        with open(f'./src/modules/{name}/{name}.service.ts', 'w') as file: # Use file to refer to the file object
            file.write(service)
