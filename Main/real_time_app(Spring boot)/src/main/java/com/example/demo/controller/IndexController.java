package com.example.demo.controller;

import com.example.demo.service.*;

import java.io.IOException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class IndexController {
	
	@Autowired
    private HbaseService hbaseService;
	
	@GetMapping("/")
	public String index(Model model) throws IOException {
        model.addAttribute("lastRecord", hbaseService.getLastRecordFromHBase());
		return "index";
	}

}
